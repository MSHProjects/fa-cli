# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
# Define the output directory
# Default to '_build' if READTHEDOCS_OUTPUT is not set
output_dir = os.environ.get('READTHEDOCS_OUTPUT', '_build')
html_output_dir = os.path.join(output_dir, 'html')

# Update the configuration to use the html_output_dir
html_context = {
    'build_dir': html_output_dir,
}

sys.path.insert(0, os.path.abspath('..'))
project = 'fa-cli'
copyright = '2024, Soulaimen Hammami'
author = 'Soulaimen Hammami'
release = '1.1.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
