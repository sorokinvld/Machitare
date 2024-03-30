import argparse
import asyncio
import json
import os

from anthropic import AsyncAnthropic
from openai import AsyncOpenAI

# Semaphores for rate limiting
openai_semaphore = asyncio.Semaphore(10)
anthropic_semaphore = asyncio.Semaphore(2)
local_semaphore = asyncio.Semaphore(1)

# Initialize clients
anthropic_client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

openai_client = AsyncOpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

local_client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="http://localhost:1235/v1",
)

SYSTEM_PROMPT = """You are a general AI assistant. I will ask you a question. Report your thoughts, and finish your answer with the following template: FINAL ANSWER: [YOUR FINAL ANSWER].
YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings.
If you are asked for a number, don’t use comma to write your number neither use units such as $ or percent sign unless specified otherwise.
If you are asked for a string, don’t use articles, neither abbreviations (e.g. for cities), and write the digits in plain text unless specified otherwise.
If you are asked for a comma separated list, apply the above rules depending of whether the element to be put in the list is a number or a string.
"""


async def local_model(question, model):
    async with local_semaphore:
        chat_completion = await local_client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content


async def openai_model(question, model):
    async with openai_semaphore:
        chat_completion = await openai_client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": question},
            ],
            model=model,
        )
        return chat_completion.choices[0].message.content


async def anthropic_model(question, model):
    async with anthropic_semaphore:
        chat_completion = await anthropic_client.messages.create(
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[
                {"role": "user", "content": [{"type": "text", "text": question}]}
            ],
            model=model,
        )
        return chat_completion.content[0].text


async def process_line_async(line, ai_function, model_name):
    data = json.loads(line)
    question = data.get("Question", "")
    final_answer = data.get("Final answer", "")

    ai_answer = await ai_function(question, model_name)

    is_correct = ai_answer.strip().lower() == final_answer.strip().lower()
    return is_correct


async def evaluate_model_async(ai_function, model_name, file_path):
    results = []
    with open(file_path, "r") as file:
        lines = file.readlines()

    tasks = [process_line_async(line, ai_function, model_name) for line in lines]
    for result in await asyncio.gather(*tasks):
        results.append(result)

    correct_answers = sum(results)
    total_questions = len(results)
    percentage_correct = (
        (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    )

    return percentage_correct, correct_answers, total_questions


async def compare_models_async(model_specs, file_path):
    model_performance = {}
    tasks = [
        evaluate_model_async(ai_function, model_name, file_path)
        for ai_function, model_name in model_specs
    ]
    results = await asyncio.gather(*tasks)

    for (ai_function, model_name), ans in zip(model_specs, results):
        accuracy, count, total_questions = ans
        model_name_str = f"{ai_function.__name__} - {model_name}"
        model_performance[model_name_str] = accuracy
        print(f"{model_name_str} accuracy: {accuracy:.2f}% ({count}/{total_questions})")

    best_model = max(model_performance, key=model_performance.get)  # type: ignore
    print(
        f"Best performing model: {best_model} with {model_performance[best_model]:.2f}% accuracy"
    )


model_specs = [
    # (openai_model, "gpt-3.5-turbo"),
    # (openai_model, "gpt-4-0125-preview"),
    (anthropic_model, "claude-3-opus-20240229"),
    # (anthropic_model, "claude-3-sonnet-20240229"),
    # (anthropic_model, "claude-3-haiku-20240307"),
    # (local_model, "TheBloke/phi-2-GGUF/phi-2.Q8_0.gguf")
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data-dir",
        type=str,
        help="Path to GAIA data directory",
        default="../GAIA/2023/validation",
    )
    args = parser.parse_args()

    file_path = f"{args.data_dir}/metadata.jsonl"

    asyncio.run(compare_models_async(model_specs, file_path))
