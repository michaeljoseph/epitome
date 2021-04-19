# epitome 👌

A [`cookiecutter`] python project.

## Generated Project
```
$ tree -a example/ -I 'dist/|*pyc*|*direnv*|*.tox*'

example/
├── .cookiecutterrc
├── .coverage
├── .envrc
├── .github
│   └── workflows
│       └── test.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .tool-versions
├── .travis.yml
├── README.md
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── src
│   └── example
│       ├── __init__.py
│       └── cli.py
├── test-reports
│   └── junit.xml
├── tests
│   └── test_example.py
└── tox.ini

6 directories, 17 files
```

## Development

```bash
# in a virtualenv
pip install poetry tox
tox
```

[`cookiecutter`]:https://github.com/cookiecutter/cookiecutter
