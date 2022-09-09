import rich_click as click
from .build import build_projects


@click.group()
def cli():
    pass


def main():
    cli()


@cli.command()
def build():
    build_projects


if __name__ == "__main__":
    main()
