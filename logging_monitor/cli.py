import click
from logging_monitor.common import add_log


@click.command()
@click.option("--level", help="Log level")
@click.option("--message", help="Log message")
def log(level, message):
    msg = add_log(level, message)
    click.echo(msg)


if __name__ == "__main__":
    log()
