# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.5] - 2025-09-13

### Added
- Added `--version` flag to display current version
- Version is now automatically read from package metadata to stay in sync with `pyproject.toml`

### Fixed
- Fixed bug where `Path` was not imported, causing import errors
- Fixed duplicate parameter warning for `-p` flag by changing `--template` shorthand to `-tp`

### Added
- Added `--deps` option to specify additional Python dependencies (space-separated)

### Changed
- Improved version detection system to work reliably with different installation methods
- Updated Tailwind CSS CDN link to new `@tailwindcss/browser@4` URL