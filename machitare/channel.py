from abc import ABC, abstractmethod


class Channel(ABC):
    @abstractmethod
    async def send(self, message):
        pass

    @abstractmethod
    async def receive(self):
        pass
