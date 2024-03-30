import asyncio
import socket
from .streaming_pb2 import StreamData, Event


class Client:
    def __init__(self, tcp_port, udp_port):
        self.tcp_port = tcp_port
        self.udp_port = udp_port

    async def tcp_send(self, event_type, content):
        reader, writer = await asyncio.open_connection("127.0.0.1", self.tcp_port)

        event = Event(type=event_type, content=content)
        stream_data = StreamData()
        stream_data.event.CopyFrom(event)

        print(f"Send: {stream_data}")
        writer.write(stream_data.SerializeToString())
        await writer.drain()

        data = await reader.read(100)
        print(f"Received: {data.decode()}")

        # print('Closing the connection')
        # writer.close()

    def udp_send(self, event_type, content):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        event = Event(type=event_type, content=content)
        stream_data = StreamData()
        stream_data.event.CopyFrom(event)

        udp_socket.sendto(stream_data.SerializeToString(), ("127.0.0.1", self.udp_port))

        data, addr = udp_socket.recvfrom(1024)
        print(f"Received: {data.decode()}")
