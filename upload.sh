# Simple commmands to upload the files into pypi.
PYTHON=$(which python3)
$PYTHON -m pip install --user --upgrade pip twine setuptools wheel
$PYTHON ./setup.py sdist bdist_wheel
$PYTHON -m twine upload --username $PYPI_USER --password $PYPI_PASSWORD ./dist/*