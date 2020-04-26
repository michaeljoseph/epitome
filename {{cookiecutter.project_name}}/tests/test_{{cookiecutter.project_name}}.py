from click.testing import CliRunner
from {{ cookiecutter.project_name }} import {{ cookiecutter.project_name }}


def test_{{ cookiecutter.project_name }}_hello():
    result = CliRunner().invoke({{ cookiecutter.project_name }}, ['hello', 'testing'])
    assert result.exit_code == 0
    assert result.output == 'Hello testing\n'
