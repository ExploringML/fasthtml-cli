from fasthtml_cli.template_builder import TemplateBuilder
from fasthtml_cli.gallery_fetcher import GalleryFetcher
from fasthtml_cli import toml

def create_main_py(name: str, template: str, tailwind: bool, reload: bool, pico: bool, deps: str = "", gallery: str = ""):
    """Create the main.py file using the flexible template builder or gallery example."""
    
    # Gallery mode: ignore all other template options
    if gallery:
        fetcher = GalleryFetcher()
        try:
            example = fetcher.fetch_example(gallery)
            return example['code']
        except Exception as e:
            print(f"Warning: Failed to fetch gallery example '{gallery}': {e}")
            print("Falling back to basic template...")
            # Fall through to regular template mode
    
    # Regular template mode
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

def create_pyproject_toml(name: str, deps: str = "", gallery: str = ""):
    """Create the pyproject.toml file with selected config options."""
    
    # Gallery mode: use gallery dependencies
    if gallery:
        fetcher = GalleryFetcher()
        try:
            example = fetcher.fetch_example(gallery)
            dependencies = example['dependencies']
            return toml.config(name, dependencies)
        except Exception as e:
            print(f"Warning: Failed to fetch gallery dependencies for '{gallery}': {e}")
            print("Using basic FastHTML dependencies...")
            # Fall through to regular mode
    
    # Regular mode: use template builder
    builder = TemplateBuilder(name)
    if deps:
        custom_deps = [dep.strip() for dep in deps.split() if dep.strip()]
        builder.add_dependencies(custom_deps)
    
    dependencies = builder.build_pyproject_toml()
    return toml.config(name, dependencies)