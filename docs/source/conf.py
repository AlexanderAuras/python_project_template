"""Config for sphinx document generation."""

from importlib.metadata import version as metadata_version

import toml


project = toml.load("../../pyproject.toml")["project"]["name"]
with open("../../LICENSE") as file:
    file.readline()
    file.readline()
    copyright = file.readline()[10:].replace(" ", ", ", 1)
author = toml.load("../../pyproject.toml")["project"]["authors"][0]["name"]
release = metadata_version(project)
version = ".".join(release.split(".")[:2])

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.inheritance_diagram"]

templates_path = ["_templates"]
exclude_patterns = []

napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

html_theme = "alabaster"
html_static_path = ["_static"]

autodoc_default_options = {"show-inheritance": True, "members": "var1, var2", "member-order": "bysource", "special-members": "__init__", "undoc-members": True, "exclude-members": "__weakref__", "imported-members": True}
