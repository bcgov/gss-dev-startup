# Getting started with UV on WSL Ubuntu
UV is a fast Python package and project manager --
[read uv docs](https://docs.astral.sh/uv/)

## Installation
``` bash
# install curl
sudo curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Creating a quick python project
``` bash
# make a project folder
mkdir my-uv-project
cd my-uv-project
uv init --bare --python=3.12 # minimum project metadata with python versin =>3.12
```
### Comparison of `uv init` Commands

| `uv init --bare --python=3.12` | `uv init --python=3.12` |
|--------------------------------|---------------------------|
| Creates only a minimal `pyproject.toml`. | Creates a full project scaffold including README, main script (you can change the name), and pyproject config. |

#### `uv init --bare --python=3.12`
```
pyproject.toml
```

#### `uv init --python=3.12`
```
README.md
main.py
pyproject.toml
```

## Adding packages with uv add
This will create a venv, add pandas, and update project.toml
```bash
uv add pandas
```

## Working with others
Example: you clone this project and want to start working with \demo-project
```bash
cd demo-project
uv sync
```

## Running your project with UV
UV can run your project without going through venv activate
```bash
uv run python demo.py
```

The venv can also be activated and used traditionally through cmd or code editors
```bash
cd demo-project
source venv/bin/activate
python demo.py
```