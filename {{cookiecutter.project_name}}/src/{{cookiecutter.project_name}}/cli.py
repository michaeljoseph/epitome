import logging

import click


@click.option('--debug', help='Enables debug logging.', is_flag=True, default=False)
@click.group(context_settings=dict(help_option_names=[u'-h', u'--help']))
def main(debug: bool):
    """{{ cookiecutter.description }}"""
    logging.basicConfig(
        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
        level=logging.DEBUG if debug else logging.INFO,
    )


@main.command()
@click.argument('your_name')
def hello(your_name: str):
    print(f'Hello {your_name}')
