import asyncio
import socket

class Client:
    def __init__(self, tcp_port, udp_port):
        self.tcp_port = tcp_port
        self.udp_port = udp_port

    async def tcp_send(self, message):
        reader, writer = await asyncio.open_connection('127.0.0.1', self.tcp_port)

        print(f'Send: {message}')
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)
        print(f'Received: {data.decode()}')

        # print('Closing the connection')
        # writer.close()

    def udp_send(self, message):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(message.encode(), ('127.0.0.1', self.udp_port))

        data, addr = udp_socket.recvfrom(1024)
        print(f'Received: {data.decode()}')
