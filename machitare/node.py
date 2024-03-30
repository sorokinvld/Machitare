import asyncio
import resource
from multiprocessing import Process

import machitare.channel


class Node:
    def __init__(self, name):
        self.name = name
        self.channels = {}
        self.tasks = {}  # Keep track of listening tasks for each channel

    async def subscribe(self, channel_name, channel: machitare.channel.Channel):
        self.channels[channel_name] = channel
        # Start a listening task for the channel
        self.tasks[channel_name] = asyncio.create_task(self._listen(channel_name))

    async def unsubscribe(self, channel_name):
        if channel_name in self.channels:
            # Cancel the listening task for this channel
            self.tasks[channel_name].cancel()
            # Remove the task and channel from the respective dictionaries
            del self.tasks[channel_name]
            del self.channels[channel_name]

    async def send(self, channel_name, message):
        if channel_name in self.channels:
            await self.channels[channel_name].send(message)

    async def _listen(self, channel_name):
        # Continuously listen for messages on the channel
        while True:
            message = await self.channels[channel_name].receive()
            await self.process(message)

    async def process(self, message):
        print(f"Processing: {message}")
        await asyncio.sleep(0)  # simulate processing time

    def run(self, cpu_time, memory_size):
        p = Process(target=self.start, args=(cpu_time, memory_size))
        p.start()

    def start(self, cpu_time, memory_size):
        # Manage the resource limit for the process
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_time, cpu_time))
        resource.setrlimit(
            resource.RLIMIT_AS, (memory_size * 1024 * 1024, memory_size * 1024 * 1024)
        )

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
        loop.close()

    async def main(self):
        while True:
            await asyncio.sleep(1)  # This sleep is just to keep the loop running
