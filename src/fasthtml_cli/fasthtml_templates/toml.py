def config(name: str = "", deps: str = ""):
    # Base dependencies
    dependencies = ["python-fasthtml"]
    
    # Add custom dependencies if provided
    if deps:
        custom_deps = [dep.strip() for dep in deps.split() if dep.strip()]
        dependencies.extend(custom_deps)
    
    # Format dependencies for TOML
    deps_str = ', '.join([f'"{dep}"' for dep in dependencies])
    
    return f"""[project]
name = "{name}"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [{deps_str}]"""