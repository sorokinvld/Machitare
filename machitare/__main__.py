import click
import threading
import asyncio

@click.group()
def cli():
    pass

@cli.command()
def server():
    from .server import Server

    server = Server(8888, 9999)
    tcp_thread = threading.Thread(target=asyncio.run, args=(server.start_tcp_server(),))
    udp_thread = threading.Thread(target=server.start_udp_server)

    tcp_thread.start()
    udp_thread.start()

    tcp_thread.join()
    udp_thread.join()

@cli.command()
def client():
    from .client import Client

    client = Client(8888, 9999)
    asyncio.run(client.tcp_send('Hello TCP Server!'))
    client.udp_send('Hello UDP Server!')


if __name__ == "__main__":
    cli()
