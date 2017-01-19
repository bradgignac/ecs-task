import sys

import click

from ecstask import commands


@click.group()
def run():
    pass


@run.command(help='Generate a task definition from a template')
@click.argument('template', type=click.File(), default=sys.stdin)
@click.option('--var', multiple=True, type=(str, str))
def generate(template, var):
    variables = dict((x, y) for x, y in var)
    print(commands.generate(template, variables))