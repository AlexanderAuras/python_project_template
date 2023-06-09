# Template

![tests-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2Fpytest.json)
![coverage-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2Fpytest_cov.json)
![pyright-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2Fpyright.json)
![bandit-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2Fbandit.json)
![pycodestyle-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2Fpycodestyle.json)
![pydocstyle-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2Fpydocstyle.json)

## Customization
 - Customize _pyproject.toml_ (don't forget `[tool.pytest.ini_options] addpots = <...> --cov=[NAME] <...>`)
 - Custom _LICENSE_ (Third line must match `Copyright <YEAR> <NAME>` (or further changes are needed in _docs/source/conf.py_))
 - Customize _README.md_ (change badge sources)
 - Run `git branch -b dev`
 - Customize requirements.txt

## User installation
Via pip and PyPI:
```
pip install 
```
Or build from source:
```
git clone <URL>
python -m pip install --upgrade build
python -m build
python -m pip install .
```
To build the documentation:
```
(cd ./docs; make html)
```

## Development setup
0. [OPTIONAL] For the greatest comfort install Visual Studio Code and these plugins:
    - Python/Pylance/isort/Jupyter (Microsoft) _combined in the python extension_ pack
    - Coverage Gutters (ryanluker)
    - autoDocstring - Python Docstring Generator (Nils Werner)
    - Todo Tree (Gruntfuggly)<br/><br/>

1. Clone repository
    ```
    git clone <URL>
    cd <FOLDER>
    ```

1. Create virtual environment
    ```
    python -m venv ./.venv
    . ./.venv/bin/activate
    ```

1. Setup
    ```
    git checkout dev
    python -m pip install --upgrade pip
    python -m pip install --upgrade build
    python -m build
    python -m pip install --editable .[dev]
    ```

1. Develop
    1. New branch
        ```
        git merge master
        git checkout -b [feature|bugfix]/***
        ```
        or 
        ```
        git checkout master
        git checkout -b hotfix/***
        ```

    1. Format+Lint
        ```
        python -m black src tests
        python -m pycodestyle src tests
        python -m pydocstyle src
        python -m bandit -r -c pyproject.toml src
        python -m pyright src
        ```

    1. Test
        ```
        python -m pytest
        ```

    1. Commit
        ```
        git commit -m "..." 
        git push
        ```

    1. When done: Merge
        ```
        git pull
        git merge [dev|master]
        git checkout [dev|master]
        git merge <branch>
        git branch -d <branch>
        git push
        ```

1. Document
    ```
    nano CHANGELOG.md
    python badges.py
    ```

1. Publish
    ```
    git commit -m "..."
    git push
    git tag -a vX.Y.Z -m "Version X.Y.Z"
    git push origin vX.Y.Z
    python -m build
    python -m twine upload --repository hello_world dist/* --username <USER> --password *****
    ```

1. Deactivate environment
    ```
    . deactivate
    ```

## TODO
- Rework badges.py
- Dockerfile