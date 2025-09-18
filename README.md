# oh-my-logo-py

A Python port of [oh-my-logo](https://github.com/shinshin86/oh-my-logo).

## Development Workflow

This project is managed using `uv` and shell scripts in the `scripts` directory.

### 1. Install Dependencies

First, run the following command to create a virtual environment and install all dependencies.

```bash
./scripts/install.sh
```

### 2. Run the CLI Tool

Use the `run.sh` script to execute `oh-my-logo-py`.

**Basic Usage**

```bash
./scripts/run.sh "Hello World"
```

**With Options**

```bash
./scripts/run.sh "hello, world!" -p sunset --filled
./scripts/run.sh "lazy fox" -p purple-red --filled -f slick
./scripts/run.sh "lorem ipsum" --filled --gallery
```

### 3. Development Commands

Run the scripts in the `scripts` directory for development tasks.

**Format Code and Organize Imports**

```bash
./scripts/format.sh
```

**Static Analysis and Linter**

```bash
./scripts/check.sh
```

**Type Checking**

```bash
./scripts/typecheck.sh
```

## Usage as a library

This project can also be used as a library in other Python projects.

### Example

Import and use the `oh_my_logo` function as shown below.

```python
from oh_my_logo_py import oh_my_logo

# Display the logo with text and default style
oh_my_logo("Hello World")

# Display with a specified palette
oh_my_logo("Pythonista", palette_name="grad-purple")

# Font and fill options can also be specified
oh_my_logo("FILLED", palette_name="mono", font="block", filled=True)
```

The `oh_my_logo` function takes the following arguments:

-   `text` (str): The text to display.
-   `palette_name` (str): The name of the color palette to use (default: `"grad-blue"`).
-   `font` (str): The name of the font to use with `pyfiglet` or `cfonts` (default: `"standard"`).
-   `filled` (bool): Whether to enable filled mode using `cfonts` (default: `False`).

## Development with `uv`

If you prefer not to use the shell scripts, you can run the development commands directly with `uv`.

### 1. Create virtual environment and install dependencies

```bash
# Create virtual environment
uv venv

# Activate the virtual environment (optional, as `uv run` handles it)
source .venv/bin/activate

# Install dependencies
uv pip install -e ".[dev]"
```

### 2. Run the CLI Tool

```bash
uv run oh-my-logo-py "Hello World" -p sunset
```

### 3. Development Commands

-   **Format & Lint (with auto-fix):**

```bash
uv run ruff check . --fix
uv run ruff format .
```

-   **Type Checking:**

```bash
uv run pyright
```
