from pathlib import Path
import typer
from typing_extensions import Annotated
from fasthtml_cli.utils import create_main_py, create_pyproject_toml

def get_version():
    """Get version from package metadata"""
    try:
        from importlib.metadata import version
        return version("fh-init")
    except Exception:
        return "Error: Version not found"

app = typer.Typer()

def version_callback(value: bool):
    if value:
        print(f"fh-init version {get_version()}")
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
    version: Annotated[bool, typer.Option("--version", callback=version_callback, help="Show version and exit.")] = False,
    ):
    """
    Scaffold a new FastHTML application.
    """

    # Create the project path.
    path = Path(name)

    # Check if directory exists.
    if path.exists():
        print(f"Error: Directory '{name}' already exists")
        return

    try:
        # Create directory
        path.mkdir(parents=True)
        
        # Create main.py
        main_file = path/'main.py'
        if main_file.exists():
            print(f"Error: {main_file} already exists, skipping")
        else:
            main_file.write_text(create_main_py(name, template, tailwind, reload, pico, deps))

        # Create pyproject.toml if uv is enabled.
        if uv:
            pyproject_file = path/'pyproject.toml'
            if pyproject_file.exists():
                print(f"Error: {pyproject_file} already exists, skipping")
            else:
                pyproject_file.write_text(create_pyproject_toml(name, deps))
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