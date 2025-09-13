from fasthtml_cli.template_builder import TemplateBuilder
from fasthtml_cli import toml

def create_main_py(name: str, template: str, tailwind: bool, reload: bool, pico: bool, deps: str = ""):
    """Create the main.py file using the flexible template builder."""
    
    builder = TemplateBuilder(name)
    
    # Add features based on options
    if tailwind:
        builder.add_tailwind()
    elif pico:  # pico is default unless tailwind is used
        builder.add_pico()
    
    if reload:
        builder.add_live_reload()
    
    # Add custom dependencies
    if deps:
        custom_deps = [dep.strip() for dep in deps.split() if dep.strip()]
        builder.add_dependencies(custom_deps)
    
    return builder.build_main_py()

def create_pyproject_toml(name: str, deps: str = ""):
    """Create the pyproject.toml file with selected config options."""
    
    # Use the template builder to get dependencies for consistency
    builder = TemplateBuilder(name)
    if deps:
        custom_deps = [dep.strip() for dep in deps.split() if dep.strip()]
        builder.add_dependencies(custom_deps)
    
    dependencies = builder.build_pyproject_toml()
    return toml.config(name, dependencies)