# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GSAS-II web documentation'
copyright = '2024 by Argonne National Laboratory'
author = 'Brian H. Toby'
release = '1.0'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['myst_parser']
#extensions = ['sphinxnotes.strike']  # not used any more
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
#    "sphinx.ext.viewcode",
#    "sphinx.ext.todo",
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
import sphinx_readable_theme
html_theme = 'readable'
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_css_files = [
    '../../../webdocs.css',
]
