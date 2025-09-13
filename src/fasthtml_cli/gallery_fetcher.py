"""
FastHTML Gallery integration for fetching example code from the official repository.
"""
import re
import ast
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class GalleryFetcher:
    """Fetches and analyzes FastHTML examples from the official gallery repository."""
    
    BASE_URL = "https://raw.githubusercontent.com/AnswerDotAI/FastHTML-Gallery/main/examples"
    GITHUB_API_URL = "https://api.github.com/repos/AnswerDotAI/FastHTML-Gallery/contents/examples"
    
    def __init__(self):
        self.session = None  # Will be set up when needed
    
    def validate_slug(self, slug: str) -> bool:
        """Validate that a gallery slug has the correct format."""
        if not slug or "/" not in slug:
            return False
        
        parts = slug.split("/")
        if len(parts) != 2:
            return False
            
        category, example = parts
        return bool(category.strip() and example.strip())
    
    def fetch_example_code(self, slug: str) -> str:
        """Fetch the app.py code from a gallery example."""
        if not self.validate_slug(slug):
            raise ValueError(f"Invalid gallery slug format: '{slug}'. Expected format: 'category/example'")
        
        url = f"{self.BASE_URL}/{slug}/app.py"
        
        try:
            import requests
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except ImportError:
            raise ImportError("requests library is required for gallery functionality")
        except requests.RequestException as e:
            # Sanitize error message to avoid information disclosure
            if "404" in str(e):
                raise ConnectionError(f"Gallery example '{slug}' not found")
            else:
                raise ConnectionError(f"Failed to fetch gallery example '{slug}': Network error")
    
    def extract_dependencies(self, code: str) -> List[str]:
        """Extract import statements and infer dependencies from FastHTML code."""
        dependencies = ["python-fasthtml"]  # Always include FastHTML
        
        # Parse imports using AST
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        dep = self._map_import_to_dependency(alias.name)
                        if dep and dep not in dependencies:
                            dependencies.append(dep)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        dep = self._map_import_to_dependency(node.module)
                        if dep and dep not in dependencies:
                            dependencies.append(dep)
        except SyntaxError:
            # If code parsing fails, fall back to regex
            dependencies.extend(self._extract_dependencies_regex(code))
        
        return dependencies
    
    def _extract_dependencies_regex(self, code: str) -> List[str]:
        """Fallback dependency extraction using regex patterns."""
        dependencies = []
        
        # Common patterns to look for
        patterns = {
            r'import\s+(numpy|np)': 'numpy',
            r'from\s+numpy': 'numpy',
            r'import\s+pandas': 'pandas',
            r'from\s+pandas': 'pandas',
            r'import\s+requests': 'requests',
            r'from\s+requests': 'requests',
            r'import\s+httpx': 'httpx',
            r'from\s+httpx': 'httpx',
            r'fastsql': 'fastsql',
            r'apswutils': 'apswutils',
            r'matplotlib': 'matplotlib',
            r'seaborn': 'seaborn',
        }
        
        for pattern, dep in patterns.items():
            if re.search(pattern, code, re.IGNORECASE):
                if dep not in dependencies:
                    dependencies.append(dep)
        
        return dependencies
    
    def _map_import_to_dependency(self, import_name: str) -> Optional[str]:
        """Map Python import names to pip package names."""
        # Common mappings where import name != pip package name
        mappings = {
            'cv2': 'opencv-python',
            'PIL': 'pillow',
            'sklearn': 'scikit-learn',
            'yaml': 'pyyaml',
            'bs4': 'beautifulsoup4',
            'flask': 'flask',
            'django': 'django',
            'fastapi': 'fastapi',
            'starlette': 'starlette',
            # FastHTML ecosystem
            'fasthtml': 'python-fasthtml',
            'fastsql': 'fastsql',
            'apswutils': 'apswutils',
            # Common data science
            'numpy': 'numpy',
            'pandas': 'pandas',
            'matplotlib': 'matplotlib',
            'seaborn': 'seaborn',
            'requests': 'requests',
            'httpx': 'httpx',
        }
        
        # Get base module name (before any dots)
        base_import = import_name.split('.')[0]
        
        # Skip standard library modules
        stdlib_modules = {
            'os', 'sys', 'json', 'csv', 'sqlite3', 'uuid', 'datetime', 
            'pathlib', 'typing', 'collections', 'itertools', 'functools',
            'asyncio', 're', 'random', 'math', 'time', 'io', 'base64'
        }
        
        if base_import in stdlib_modules:
            return None
            
        return mappings.get(base_import, base_import)
    
    def fetch_example(self, slug: str) -> Dict[str, any]:
        """
        Fetch a complete gallery example with code and metadata.
        
        Returns:
            {
                'code': str,           # The app.py code
                'dependencies': list,  # Detected dependencies
                'slug': str           # The original slug
            }
        """
        code = self.fetch_example_code(slug)
        dependencies = self.extract_dependencies(code)
        
        return {
            'code': code,
            'dependencies': dependencies,
            'slug': slug
        }
    
    def list_categories(self) -> List[str]:
        """
        List available gallery categories (future feature).
        For now, returns known categories.
        """
        return [
            "applications",
            "dynamic_user_interface_(htmx)", 
            "svg",
            "todo_series",
            "visualizations", 
            "widgets"
        ]