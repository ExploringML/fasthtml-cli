from pathlib import Path
import re
import typer
from typing_extensions import Annotated
from fasthtml_cli.utils import create_main_py, create_pyproject_toml

def sanitize_project_name(name: str) -> str:
    """Sanitize project name to prevent path traversal and ensure valid directory names."""
    # Allow only alphanumeric, hyphens, underscores, and dots
    # Remove any path separators or parent directory references
    sanitized = re.sub(r'[^a-zA-Z0-9._-]', '', name)
    
    # Remove leading dots to prevent hidden files
    sanitized = sanitized.lstrip('.')
    
    # Ensure name is not empty after sanitization
    if not sanitized:
        return "fasthtml-app"
    
    return sanitized

def get_version():
    """Get version from package metadata"""
    try:
        from importlib.metadata import version
        return version("fh-cli")
    except Exception:
        return "Error: Version not found"

app = typer.Typer()

def version_callback(value: bool):
    if value:
        print(f"fh-cli version {get_version()}")
        raise typer.Exit()

@app.command()
def main(
    name: Annotated[str, typer.Argument(help="FastHTML app name.")],
    template: Annotated[str, typer.Option("--template", "-tp", help="The name of the FastHTML template to use.")] =  "base",
    reload: Annotated[bool, typer.Option("--reload", "-r", help="Enable live reload.")] = False,
    pico: Annotated[bool, typer.Option("--pico", "-p", help="Enable Pico CSS.")] = True,
    uv: Annotated[bool, typer.Option(help="Use uv to manage project dependencies.")] = True,
    tailwind: Annotated[bool, typer.Option("--tailwind", "-t", help="Enable Tailwind CSS.")] = False,
    deps: Annotated[str, typer.Option("--deps", "-d", help="Space-separated list of Python dependencies to add (e.g., 'pandas numpy requests').")] = "",
    gallery: Annotated[str, typer.Option("--gallery", "-g", help="Use a FastHTML Gallery example (e.g., 'todo_series/beginner'). When used, other template options are ignored.")] = "",
    version: Annotated[bool, typer.Option("--version", callback=version_callback, help="Show version and exit.")] = False,
    ):
    """
    Scaffold a new FastHTML application.
    """

    # Sanitize project name to prevent path traversal
    sanitized_name = sanitize_project_name(name)
    if sanitized_name != name:
        print(f"Error: Invalid project name. Only alphanumeric characters, hyphens, and underscores are allowed.")
        return
    
    # Create the project path.
    path = Path(sanitized_name)

    # Check if directory exists.
    if path.exists():
        print(f"Error: Directory '{sanitized_name}' already exists")
        return

    try:
        # Create directory
        path.mkdir(parents=True)
        
        # Create main.py
        main_file = path/'main.py'
        if main_file.exists():
            print(f"Error: {main_file} already exists, skipping")
        else:
            main_file.write_text(create_main_py(name, template, tailwind, reload, pico, deps, gallery))

        # Create pyproject.toml if uv is enabled.
        if uv:
            pyproject_file = path/'pyproject.toml'
            if pyproject_file.exists():
                print(f"Error: {pyproject_file} already exists, skipping")
            else:
                pyproject_file.write_text(create_pyproject_toml(name, deps, gallery))
    except PermissionError:
        print(f"Error: Permission denied creating {name}")
    except OSError as e:
        print(f"Error creating project: {e}")
    else:
        print(f"\n✨ New FastHTML app created successfully!")

        print("\nTo get started, enter:\n")
        print(f"  $ cd {name}")

        if uv:
            print("  $ uv run main.py\n")
        else:
            print("  $ python main.py\n")


if __name__ == "__main__":
    app()