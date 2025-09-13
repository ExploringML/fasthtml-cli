# FastHTML CLI

See the 'Development' section of README.md for details on setting up the development version of the CLI for local testing.

# Update MD Files

As you make changes ALWAYS keep the README.md and CHANGELOG.md files up to date. This is very important to keep users informed of updates. Make sure you only update the changelog section relating to the current version specified in pyproject.toml.

# Publish to PyPi

Here are the instructions to push new CLI versions to PyPi.

Delete the dist folder and run:

```
uv build
```

Then make sure the PyPi token has been set with:

```
export UV_PUBLISH_TOKEN=pypi-AgEIc...
```

Publish to PyPi with:

```
uv publish
```

# Resources

- https://youtu.be/qh98qOND6MI