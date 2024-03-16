# ESCAPE ROOM FOR RECRUITERS IT
Exciting virtual escape room designed for programming enthusiasts and tech recruiters.

## Table of contents

- [Initial steps](#initial-steps)
- [Setup git](#setup-git)
- [Set up environment](#set-up-environment)
- [Style guides](#style-guides)
- [Reset migrations](#reset-migrations)


## Initial steps

If you're going to contribute to this repo, follow the steps below.

- Set up your git config locally.
- Read style guide docs.
- Set up all tools needed.
- Interact with the database.

## Setup git
Set a name on your `local` git config

```bash
# e.g.:
$ git config --local user.name "{{ first name }} {{ last name }}"
```

Set an email on your `local` git config

```bash
# suggestion, use your private GitHub email
# e.g.:
$ git config --local user.email "xxxxxxxxxx@users.noreply.github.com"
```

Set a pull strategy on your `local` git config, avoid a warning on every `git pull` since version `2.27`

```bash
$ git config --local pull.rebase false
```

References:

- [How to deal with this git warning? “Pulling without specifying how to reconcile divergent branches is discouraged”](https://stackoverflow.com/q/62653114/)


## Set up environment
Install and set the right python version
```bash
curl https://pyenv.run | bash
pyenv install 3.11
pyenv local 3.11
```
Install and set poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry env use 3.11
poetry shell
poetry install
```

Use the poetry to locally run the web app
```bash
poetry run uvicorn app.main:start
```

## Verifying the Application

To verify that the application is running correctly, you can use the following URLs:

- [http://0.0.0.0:8000/health-status](http://0.0.0.0:8000/health-status)
- [http://localhost:8000/health-status](http://localhost:8000/health-status)

These URLs will display the health status of the application.

## Style guides

In the Python ecosystem, it is strongly suggested to use [PEP 8](https://www.python.org/dev/peps/pep-0008/), which is a list of suggestions to follow on any Python code. The tool that we use as a `linter` to enforce this suggestion is [flake8](https://github.com/PyCQA/flake8).

After that, considering that we are going to use [FastAPI](https://fastapi.tiangolo.com/) as a web framework. One of the suggestions is to use [isort](https://github.com/PyCQA/isort) to enforce a specific sort of technique on `import` statements

Part of the standardization that we have as a team, we're going to use [black](https://github.com/psf/black) as the code formatting, to complement PEP8 with its [code style](https://black.readthedocs.io/en/stable/the_black_code_style.html)

References:

- [zedr/clean-code-python](https://github.com/zedr/clean-code-python) - Code Cleand used in Python
- [mjhea0/awesome-fastapi](https://github.com/mjhea0/awesome-fastapi) - Multiple resources for FastAPI
- [Things about Python](https://gist.github.com/eevmanu/b2c8c49b79f02cdc1f764c1d9bdfa320)
- [JSON Naming Convention (snake_case, camelCase or PascalCase) [closed]](https://stackoverflow.com/q/5543490/)

## Running Tests and Code Verification
To run the unit tests, use the following command:
```bash
   pytest
```
To perform code verification, use the following command:
```bash
   pysen run lint && flake8 . && pylint app && autopep8 --in-place --recursive . && bandit -r . -s B101 && pytest
```
For more information, refer to the pyproject.toml file.

## Contribution
If you want to contribute to this project, follow these steps:

* Create a new branch for your contribution:
```bash
   git checkout -b my-new-feature
```
* Make the changes and commit meaningful commits.
* Push your changes to your repository:
```bash
   git push origin my-new-feature
```
* Open a Pull Request on this repository and describe your changes.

## Questions or Suggestions
If you have any questions or suggestions for additional functionality, please feel free to contact us at enlabe@gmail.com.

