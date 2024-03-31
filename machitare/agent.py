import asyncio
import os

import pydantic
from openai import AsyncOpenAI

openai_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
openai_semaphore = asyncio.Semaphore(10)


class Understanding(pydantic.BaseModel):
    task_is_possible: bool
    task_requires_team: bool
    team: list["Agent"] | None = None


class AgentConfig(pydantic.BaseModel):
    agent_name: str
    description: str
    task: str


class Thoughts(pydantic.BaseModel):
    thoughts: str
    report: str | None = None
    situation_summary: str
    task_complete: bool


class Agent:
    # Keep track of the agents thoughts
    thoughts: list[str]
    # Keep track of the agents team mates reports
    sibling_updates: list[str]
    # Keep track of the agents subordinates reports
    child_reports: list[str]
    # Keep track of the agents own reports
    my_reports: list[str]

    # TODO: Currently there is no way for parents to pass information down to children
    
    # Suation summary of the agent
    current_state: str

    keep_running: bool = True

    def __init__(
        self,
        agent_name: str,
        description: str,
        task: str,
        parent: "Agent" | None,
        model: str = "gpt-4-0125-preview",
    ):
        self.agent_name = agent_name
        self.description = description
        self.task = task
        self.parent = parent
        self.children: list[Agent] = []
        self.model = model

    async def understand_task(self):
        """
        Checks its understanding of the task it has been given
        and if the task requires a team, it creates a team.
        """
        async with openai_semaphore:
            chat_completion = await openai_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question},
                ],
                model=self.model,
                response_format={"type": "json_object"},
            )
            understanding = Understanding.model_validate_json(
                chat_completion.choices[0].message.content
            )

            if not understanding.task_is_possible:
                raise ValueError("Task is not possible")

            if understanding.task_requires_team:
                await self.create_team(understanding.team)

    async def create_team(self, team: list["Agent"]):
        for member in team.agents:
            self.children.append(
                Agent(
                    agent_name=member.agent_name,
                    description=member.description,
                    task=member.task,
                    parent=self,
                )
            )
        asyncio.gather(*[child.run() for child in self.children])

    async def send_report(self, report: str):
        """
        Send a progress report to the parent agent.
        """
        self.parent.receive_report(report)

    async def receive_report(self, report: str):
        """
        Receive a progress report from a child agent and
        propogate it to all other child agents.
        """

        # First we store the report
        self.child_reports.append(report)
        # Then we propogate the report to all children
        for child in self.children:
            await child.receive_update(report)

        # Process the latest information
        await self.think()

    async def receive_update(self, update: str):
        self.sibling_updates.append(update)
        await self.think()

    async def think(self):
        # TODO: Implement the logic to think about the task
        async with openai_semaphore:
            chat_completion = await openai_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question},
                ],
                model=self.model,
                response_format={"type": "json_object"},
            )
            thoughts = Thoughts.model_validate_json(
                chat_completion.choices[0].message.content
            )

            self.thoughts.append(thoughts.thoughts)
            self.current_state = thoughts.situation_summary
            if thoughts.task_complete:
                self.send_report(f"{self.agent_name} has completed the task")
                await self.shutdown()
            elif thoughts.report:
                await self.send_report(thoughts.report)

    async def shutdown(self):
        for child in self.children:
            await child.shutdown()
        self.keep_running = False

    async def run(self):
        # First the agent needs to understand the task it has been given
        await self.understand_task()
        while self.keep_running:
            await asyncio.sleep(1)
