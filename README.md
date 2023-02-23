# Template

![tests-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2F/pytest.json)
![coverage-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2F/pytest_cov.json)
![pyright-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2F/pyright.json)
![bandit-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2F/bandit.json)
![pycodestyle-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2F/pycodestyle.json)
![pydocstyle-badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlexanderAuras%2Fpython_project_template%2Fmaster%2F.badges%2F/pydocstyle.json)

## Customization
 - Customize _pyproject.toml_ (don't forget `[tool.pytest.ini_options] addpots = <...> --cov=[NAME] <...>`)
 - Custom _LICENSE_ (Third line must match `Copyright <YEAR> <NAME>` (or further changes are needed in _docs/source/conf.py_))
 - Customize _README.md_ (change badge sources)
 - Run `git branch -b dev`
 - Customize requirements.txt

## Installation
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
1. Create virtual environment
    ```
    python -m venv ./venv
    . ./venv/bin/activate
    ```

1. Setup
    ```
    git clone <URL>
    git checkout dev
    python -m pip install --upgrade build
    python -m build
    python -m pip install --editable .[dev]
    ```

1. Develop
    1. New branch
        ```
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
        python -m pyright
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
        ```

1. Document
    ```
    nano CHANGELOG
    python badges.py
    ```

1. Publish
    ```
    git commit -m "..."
    git push
    git tag -a vX.Y.Z -m "Version X.Y.Z"
    git push vX.Y.Z
    python -m build
    python -m twine upload --repository hello_world dist/* --username alex.aur --password *****
    ```

1. Deactivate environment
    ```
    . deactivate
    ```

## TODO
- Rework badges.py
- Dockerfile