# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.5] - 2025-09-13

### Added
- Added `--version` flag to display current version
- Version is now automatically read from package metadata to stay in sync with `pyproject.toml`
- Added `--deps` option to specify additional Python dependencies (space-separated)
- Dependencies are now automatically imported in generated main.py files with proper aliases (e.g., `pandas as pd`, `numpy as np`)
- **NEW**: Added `--gallery` option to bootstrap projects from the official [FastHTML Gallery](https://gallery.fastht.ml/)
  - Pull complete working examples with `fh-init my-app --gallery category/example`
  - Automatic dependency detection from gallery code
  - When `--gallery` is used, all other template options are ignored (by design)

### Fixed
- Fixed bug where `Path` was not imported, causing import errors
- Fixed duplicate parameter warning for `-p` flag by changing `--template` shorthand to `-tp`
- Fixed bug where `--deps` dependencies were only added to pyproject.toml but not imported in main.py
- Fixed single-item tuple syntax for headers (now properly includes trailing comma)

### Security
- Added input sanitization to prevent path traversal attacks in project names
- Enhanced error message sanitization to prevent information disclosure
- Added version constraints to dependencies to improve supply chain security
- Implemented comprehensive security audit with 0 vulnerabilities found

### Changed
- **BREAKING**: Replaced rigid template system with flexible component-based TemplateBuilder
- Improved version detection system to work reliably with different installation methods
- Updated Tailwind CSS CDN link to new `@tailwindcss/browser@4` URL
- Restructured codebase: moved toml.py and removed fasthtml_templates folder