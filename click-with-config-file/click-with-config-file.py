#!/usr/bin/python3

# template from https://jwodder.github.io/kbits/posts/click-config/
# License: Creative Commons Attribution 4.0 International License.

from configparser import ConfigParser
import click

# import json

DEFAULT_CFG = "config.ini"


def configure(ctx, param, filename):
    cfg = ConfigParser()
    cfg.read(filename)
    try:
        options = dict(cfg["options"])
    except KeyError:
        options = {}
    ctx.default_map = options


@click.command()
@click.option(
    "-c",
    "--config",
    type=click.Path(dir_okay=False),
    default=DEFAULT_CFG,
    callback=configure,
    is_eager=True,
    expose_value=False,
    help="Read option defaults from the specified INI file",
    show_default=True,
)
@click.option("-i", "--input-path", type=click.Path(exists=True), required=True)
def main(input_path):
    print("--input-path = " + input_path)


if __name__ == "__main__":
    main()
