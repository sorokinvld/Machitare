import asyncio
import threading

import click


@click.group()
def cli():
    pass


@cli.command()
def agent():
    import asyncio

    import machitare.agent

    a = machitare.agent.Agent()

    asyncio.run(a.run())


if __name__ == "__main__":
    cli()
