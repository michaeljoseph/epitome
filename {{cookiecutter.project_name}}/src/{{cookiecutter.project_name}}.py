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


@click.option('--debug', help='Enables debug logging.', is_flag=True, default=False)
@click.group(context_settings=dict(help_option_names=[u'-h', u'--help']))
def {{ cookiecutter.project_name }}(debug: bool):
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


@{{ cookiecutter.project_name }}.command()
@click.argument('your_name')
def hello(your_name: str):
    print(f'Hello {your_name}')
