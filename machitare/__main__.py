import asyncio
import threading

import click


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
@click.option("--event-type", default="Hello", help="Type of the event to send.")
@click.option(
    "--content",
    default="This is the message being sent",
    help="Content of the event to send.",
)
def client(event_type, content):
    from .client import Client

    client = Client(8888, 9999)
    asyncio.run(client.tcp_send(event_type, f"TCP: {content}"))
    client.udp_send(event_type, f"UDP: {content}")


if __name__ == "__main__":
    cli()
