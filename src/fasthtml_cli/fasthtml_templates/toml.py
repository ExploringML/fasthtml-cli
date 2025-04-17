def config(name: str = ""):
    return f"""[project]
name = "{name}"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = ["python-fasthtml"]"""