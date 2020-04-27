from click.testing import CliRunner

from example import example


def test_example_hello():
    result = CliRunner().invoke(example, ['hello', 'testing'])
    assert result.exit_code == 0
    assert result.output == 'Hello testing\n'
