import asyncio
import socket
import threading
from .streaming_pb2 import StreamData, Event


class Server:
    def __init__(self, tcp_port, udp_port):
        self.tcp_port = tcp_port
        self.udp_port = udp_port

    async def tcp_handler(self, reader, writer):
        data = await reader.read(100)
        stream_data = StreamData()
        stream_data.ParseFromString(data)
        event = stream_data.event
        addr = writer.get_extra_info("peername")

        print(f"Received {event.type} event with content {event.content} from {addr}")

        print(f"Send: {event.type} event with content {event.content}")
        writer.write(data)
        await writer.drain()

    async def udp_handler(self, data, addr):
        stream_data = StreamData()
        stream_data.ParseFromString(data)
        event = stream_data.event

        print(f"Received {event.type} event with content {event.content} from {addr}")
        print(f"Send: {event.type} event with content {event.content}")
        self.udp_socket.sendto(data, addr)

    async def start_tcp_server(self):
        server = await asyncio.start_server(
            self.tcp_handler, "127.0.0.1", self.tcp_port
        )

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        async with server:
            await server.serve_forever()

    def start_udp_server(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(("127.0.0.1", self.udp_port))

        print(f"Serving on {self.udp_socket.getsockname()}")

        while True:
            data, addr = self.udp_socket.recvfrom(1024)
            asyncio.run(self.udp_handler(data, addr))
