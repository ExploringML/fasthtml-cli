# FastHTML CLI

[![PyPI](https://img.shields.io/pypi/v/fh-init)](https://pypi.org/project/fh-init/)
[![License](https://img.shields.io/github/license/ExploringML/fasthtml-cli)](https://github.com/your-username/your-repo/blob/main/LICENSE)
[![Sponsor](https://img.shields.io/badge/Sponsor-FastHTML%20CLI-pink?logo=github)](https://github.com/sponsors/ExploringML)

Fastest way to scaffold FastHTML apps!

## Usage

To create a new FastHTML application, use the `fh-init` command. Make sure [`uv`](https://docs.astral.sh/uv/getting-started/installation/) is installed before running `uvx`:

```bash
uvx fh-init [OPTIONS] NAME
```

### Arguments

*   `NAME`: The name of your FastHTML application (required).

### Options

*   `--template, -tp TEXT`: The name of the FastHTML template to use (default: `base`).
*   `--reload, -r`: Enable live reload.
*   `--pico, -p`: Enable Pico CSS (default: `True`).
*   `--uv / --no-uv`: Use uv to manage project dependencies (default: `uv`).
*   `--tailwind, -t`: Enable Tailwind CSS.
*   `--deps, -d TEXT`: Space-separated list of Python dependencies to add (e.g., `pandas numpy requests`).
*   `--version`: Show version and exit.
*   `--install-completion`: Install tab completion for the current shell (run once to enable auto-completion).
*   `--show-completion`: Show completion script to copy or customize the installation.
*   `--help`: Show the help message and exit.

### Examples

```bash
# Create a basic app
uvx fh-init my_awesome_app

# Create an app with live reload and Tailwind CSS
uvx fh-init my_awesome_app --reload --tailwind

# Create an app with additional Python dependencies
uvx fh-init data_app --deps "pandas numpy matplotlib"
```

Then to run the FastHTML app:

```bash
cd my_awesome_app
uv run main.py
```

### Shell Completion

For a better CLI experience, you can enable tab completion:

```bash
# Install completion for your current shell (run once)
fh-init --install-completion

# After installation, you can use tab completion
fh-init <Tab>          # Shows available commands and options
fh-init --<Tab>        # Shows all available flags
```

## Development

### Initial Setup

For first-time setup:

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate
   ```

2. **Install the CLI locally in editable mode:**
   ```bash
   uv pip install -e .
   ```

### Quick Development Workflow

After making any changes to code or `pyproject.toml`:

1. **In the CLI root folder, run:**
   ```bash
   source .venv/bin/activate && uv pip install -e . --force-reinstall && uv cache clean
   ```

2. **Use the local development CLI from any other folder:**
   ```bash
   # Check version
   uvx --from <path-to-local-cli-folder> fh-init --version
   
   # Create a test project
   uvx --from <path-to-local-cli-folder> fh-init test-app
   ```
### Troubleshooting

- If uvx shows old version after changes, the single update command above should resolve it
- The `--version` flag reads from package metadata to ensure version consistency with `pyproject.toml`
