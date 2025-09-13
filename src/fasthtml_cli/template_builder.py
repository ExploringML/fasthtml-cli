class TemplateBuilder:
    """A flexible component-based template builder for FastHTML apps."""
    
    def __init__(self, name: str):
        self.name = name
        self.imports = ["from fasthtml.common import *"]
        self.headers = []
        self.app_options = []
        self.dependencies = ["python-fasthtml"]
    
    def add_tailwind(self):
        """Add Tailwind CSS support."""
        self.headers.append('Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4")')
        # Tailwind disables Pico CSS
        self.app_options = [opt for opt in self.app_options if not opt.startswith("pico=")]
        self.app_options.append("pico=False")
        return self
    
    def add_live_reload(self):
        """Add live reload support."""
        if "live=True" not in self.app_options:
            self.app_options.append("live=True")
        return self
    
    def add_pico(self):
        """Add Pico CSS support (default unless Tailwind is used)."""
        # Only add if no pico option exists and no Tailwind
        has_pico = any(opt.startswith("pico=") for opt in self.app_options)
        has_tailwind = any("tailwindcss" in header for header in self.headers)
        
        if not has_pico and not has_tailwind:
            self.app_options.append("pico=True")
        return self
    
    def add_dependencies(self, deps: list):
        """Add custom Python dependencies."""
        for dep in deps:
            if dep not in self.dependencies:
                self.dependencies.append(dep)
                # Add import statement for common packages
                import_name = self._get_import_name(dep)
                if import_name:
                    import_statement = f"import {import_name}"
                    if import_statement not in self.imports:
                        self.imports.append(import_statement)
        return self
    
    def _get_import_name(self, dep: str):
        """Get the import name for common packages."""
        # Handle common package name mappings
        common_mappings = {
            'pandas': 'pandas as pd',
            'numpy': 'numpy as np', 
            'requests': 'requests',
            'matplotlib': 'matplotlib.pyplot as plt',
            'seaborn': 'seaborn as sns',
            'scikit-learn': 'sklearn',
            'pillow': 'PIL',
            'beautifulsoup4': 'bs4',
        }
        
        # Extract base package name (remove version specifiers)
        base_dep = dep.split('>=')[0].split('==')[0].split('<')[0].strip()
        
        return common_mappings.get(base_dep, base_dep)
    
    def build_main_py(self):
        """Generate the main.py file content."""
        # Build imports
        imports = "\n".join(self.imports)
        
        # Build headers
        headers_section = ""
        if self.headers:
            headers_list = ", ".join(self.headers)
            # Ensure proper tuple syntax with trailing comma for single items
            if len(self.headers) == 1:
                headers_section = f"hdrs = ({headers_list},)\n"
            else:
                headers_section = f"hdrs = ({headers_list})\n"
        
        # Build app configuration
        app_config_parts = []
        if self.headers:
            app_config_parts.append("hdrs=hdrs")
        app_config_parts.extend(self.app_options)
        app_config = ", ".join(app_config_parts)
        
        # Default route
        default_route = '''@rt('/')
def get(): 
    return Div(
        H1("Hello, FastHTML!"), 
        P("Your app is running!")
    )'''
        
        # Assemble the complete template
        template = f"""{imports}

{headers_section}app, rt = fast_app({app_config})

{default_route}

serve()"""
        
        return template
    
    def build_pyproject_toml(self):
        """Generate the pyproject.toml dependencies list."""
        return self.dependencies