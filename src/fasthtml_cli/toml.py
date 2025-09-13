def config(name: str = "", dependencies: list = None):
    """Generate pyproject.toml content with the given dependencies."""
    if dependencies is None:
        dependencies = ["python-fasthtml"]
    
    # Format dependencies for TOML
    deps_str = ', '.join([f'"{dep}"' for dep in dependencies])
    
    return f"""[project]
name = "{name}"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [{deps_str}]"""