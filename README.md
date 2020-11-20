# uminifier
Script to convert Python files into .mpy (Micropython)

## Usage
```
usage: compilation_test.py [-h] [-o OUTPUT] [-k] [-v] filename

Convert python files into .mpy (Micropython) files.

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path or output filename
  -k, --keep            Keep any intermediate file generated.
  -v, --verbose         Print verbose output.
```

## Requirements
Modules needed installation:
```shell
pip install pyminifier>=2.1 mpy-cross>=1.12
```

## Running the tests
```shell script
pytest
```