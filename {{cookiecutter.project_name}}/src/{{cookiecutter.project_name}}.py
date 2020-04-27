import logging
from functools import partial

import click
import coloredlogs
import colorful
import emoji
import heartrate

log = logging.getLogger(__name__)
colorful.use_true_colors()
colorful.use_style('solarized')
emojize = partial(emoji.emojize, use_aliases=True)


def greeting(name: str):
    name = name if name else 'World'
    return emojize(f':wave: Hello {name}.')


@click.group(context_settings=dict(help_option_names=[u'-h', u'--help']))
@click.option('--debug', help='Enables debug logging.', is_flag=True, default=False)
@click.option(
    '--trace', help='Enables heartrate execution visualisation.', is_flag=True, default=False
)
def main(debug: bool, trace: bool):
    """{{ cookiecutter.description }}"""
    coloredlogs.install(
        fmt=(
            '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
            if debug
            else '%(asctime)s,%(msecs)d %(levelname)-8s %(message)s'
        ),
        level='DEBUG' if debug else 'INFO',
    )
    if trace:
        heartrate.trace()


@main.command()
@click.argument('your_name', required=False)
def hello(your_name: str):
    """What's your name?"""
    print(greeting(your_name))
