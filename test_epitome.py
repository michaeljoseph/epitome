import pytest

import os
from pathlib import Path


def test_epitome(cookies):
    result = cookies.bake(extra_context={
        'project_name': 'helloworld'
    })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'helloworld'
    assert result.project.isdir()

    readme_file = result.project.join('README.md')
    expected_readme_lines = [
        '# helloworld',
        '',
        'the project description',
    ]
    assert expected_readme_lines == readme_file.readlines(cr=False)


def test_generated_tree(cookies):
    # TODO: set git author config and $HOME
    result = cookies.bake()

    assert result.exception is None
    assert result.exit_code == 0

    project = Path(result.project)
    # https://stackoverflow.com/questions/54401973/pythons-pathlib-get-parents-relative-path
    generated_paths = [
        # https://stackoverflow.com/questions/53997726/can-python3s-pathlib-be-used-portably-between-linux-and-windows-systems
        str(path.relative_to(project)).replace('\\', '/')
        for path in project.rglob("*")
    ]

    assert project.joinpath('.git').exists()
    assert project.joinpath('.gitignore').exists()

    expected_paths = [
        'README.md',
        '.pre-commit-config.yaml',
        '.cookiecutterrc',
        '.envrc',
        'pyproject.toml',
        'tox.ini',
        '.travis.yml',
        'src',
        'src/skeletor.py',
        'tests',
        'tests/test_skeletor.py',
    ]
    # remove .git paths
    generated_paths = [p for p in generated_paths if not p.startswith('.git')]
    assert sorted(expected_paths) == sorted(generated_paths)
