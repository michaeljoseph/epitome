from click.testing import CliRunner
from {{cookiecutter.project_name}} import greeting, main


def test_{{cookiecutter.project_name}}_hello():
    result = CliRunner().invoke(main, ['hello', 'testing'])
    assert result.exit_code == 0
    assert result.output == '👋 Hello testing.\n'


def test_empty_name():
    assert '👋 Hello World.' == greeting('')


def test_trace(mocker):
    heartrate = mocker.patch('{{cookiecutter.project_name}}.heartrate.trace')
    result = CliRunner().invoke(main, ['--trace', 'hello'])
    assert result.exit_code == 0
    assert result.output == '👋 Hello World.\n'
    heartrate.assert_called()
