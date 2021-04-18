from click.testing import CliRunner

from {{ cookiecutter.project_name }}.cli import main


def test_hello():
    result = CliRunner().invoke(main, ['hello', 'testing'])
    assert result.exit_code == 0
    assert result.output == 'Hello testing\n'
