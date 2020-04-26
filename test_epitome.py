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
    result = cookies.bake()

    assert result.exception is None
    assert result.exit_code == 0

    project = Path(result.project)
    # https://stackoverflow.com/questions/54401973/pythons-pathlib-get-parents-relative-path
    generated_paths = [
        str(path.relative_to(project))
        for path in project.rglob("*")
    ]

    expected_paths = [
        'README.md',
        'src',
        'src/skeletor.py',
        'tests',
        'tests/test_skeletor.py',
    ]
    assert sorted(expected_paths) == sorted(generated_paths)
