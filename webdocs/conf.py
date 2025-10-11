# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GSAS-II'
copyright = '2025 by Argonne National Laboratory'
author = 'Brian H. Toby'
release = 'v5.6.0'


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
import sphinx_readable_theme
html_theme = 'readable'
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
# forces tables from being too wide in the HTML rendering (probably not needed)
# also removes bullet from toc lists
html_static_path = ['_static']
html_css_files = [
    'fix.css',
]
html_favicon = 'favicon.ico'
html_last_updated_fmt = ''
html_copy_source = False
html_scaled_image_link = True
