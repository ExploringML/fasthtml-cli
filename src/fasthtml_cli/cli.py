import typer
from pathlib import Path
from typing_extensions import Annotated
from fasthtml_cli.fasthtml_templates.base import base
from fasthtml_cli.utils import create_main_py, create_pyproject_toml

app = typer.Typer()

@app.command()
def main(
    name: Annotated[str, typer.Argument(help="FastHTML app name.")],
    template: Annotated[str, typer.Option("--template", "-p", help="The name of the FastHTML template to use.")] =  "base",
    reload: Annotated[bool, typer.Option("--reload", "-r", help="Enable live reload.")] = False,
    pico: Annotated[bool, typer.Option("--pico", "-p", help="Enable Pico CSS.")] = True,
    uv: Annotated[bool, typer.Option(help="Use uv to manage project dependencies.")] = True,
    tailwind: Annotated[bool, typer.Option("--tailwind", "-t", help="Enable Tailwind CSS.")] = False,
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
            main_file.write_text(create_main_py(name, template, tailwind, reload, pico))

        # Create pyproject.toml if uv is enabled.
        if uv:
            pyproject_file = path/'pyproject.toml'
            if pyproject_file.exists():
                print(f"Error: {pyproject_file} already exists, skipping")
            else:
                pyproject_file.write_text(create_pyproject_toml(name))
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