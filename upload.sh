#!/bin/bash
rm -rf ./build
rm -rf ./dist
rm -rf ./fa_cli.egg-info
# Run setup
python setup.py sdist bdist_wheel

# Replace these with your actual PyPI token
TWINE_USERNAME="__token__"
TWINE_PASSWORD="pypi-AgEIcHlwaS5vcmcCJGE4Mjc2MDdiLWZhOTQtNGNkMi04MTExLTE2OWIwOGMwN2U0YwACKlszLCI1MWI1ZWI3Zi01NThkLTQ2NzEtODMyMy02MGFmNDlkYzI5YWIiXQAABiDqTSORjKVY26cp5RSct8pqZGClptMw_Ol-1Bo1WvjqeA"

# Export the environment variables
export TWINE_USERNAME
export TWINE_PASSWORD

# Upload the package
twine upload dist/*

# Unset the environment variables for security reasons
unset TWINE_USERNAME
unset TWINE_PASSWORD
