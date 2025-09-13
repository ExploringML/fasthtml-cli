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
*   `--gallery, -g TEXT`: Use a FastHTML Gallery example (e.g., `todo_series/beginner`). When used, other template options are ignored.
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

# Create an app from the FastHTML Gallery
uvx fh-init my-todo --gallery todo_series/beginner
uvx fh-init my-viz --gallery visualizations/observable_plot
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

### FastHTML Gallery Integration

Bootstrap your projects with real-world examples from the official [FastHTML Gallery](https://gallery.fastht.ml/):

```bash
# Browse examples at https://gallery.fastht.ml/
# Use the format: category/example_name

# Todo applications
uvx fh-init my-todo --gallery todo_series/beginner

# Data visualizations  
uvx fh-init my-charts --gallery visualizations/observable_plot

# Interactive applications
uvx fh-init my-app --gallery applications/csv_editor
```

**Gallery Features:**
- **Complete Examples**: Get fully working FastHTML applications instantly
- **Auto Dependencies**: Required packages automatically added to `pyproject.toml`
- **No Modifications**: Gallery code copied exactly as-is for authentic examples
- **Exclusive Mode**: When using `--gallery`, other template options (`--tailwind`, `--deps`, etc.) are ignored

**Available Categories:**
- `applications/` - Full-featured apps (csv_editor, tic_tac_toe, etc.)
- `todo_series/` - Todo app examples of varying complexity
- `visualizations/` - Data visualization examples
- `widgets/` - Reusable UI components
- `svg/` - SVG and graphics examples
- `dynamic_user_interface_(htmx)/` - Advanced HTMX interactions

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
