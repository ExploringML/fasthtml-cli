Quickly scaffold FastHTML apps!

## Usage

To create a new FastHTML application, use the `fh-init` command. Make sure [`uv`](https://docs.astral.sh/uv/getting-started/installation/) is installed before running `uvx`:

```bash
uvx fh-init [OPTIONS] NAME
```

### Arguments

*   `NAME`: The name of your FastHTML application (required).

### Options

*   `--template, -p TEXT`: The name of the FastHTML template to use (default: `base`).
*   `--reload, -r`: Enable live reload.
*   `--pico, -p`: Enable Pico CSS (default: `True`).
*   `--uv / --no-uv`: Use uv to manage project dependencies (default: `uv`).
*   `--tailwind, -t`: Enable Tailwind CSS.
*   `--install-completion`: Install completion for the current shell.
*   `--show-completion`: Show completion for the current shell.
*   `--help`: Show the help message and exit.

### Example

```bash
uvx fh-init my_awesome_app --reload --tailwind
```

This command will create a new FastHTML application named `my_awesome_app` with live reload and Tailwind CSS enabled.

Then to run the FastHTML app:

```bash
cd my_awesome_app
uv run main.py
```
