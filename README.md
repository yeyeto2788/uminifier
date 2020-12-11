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

## How to use it with docker

### Converting a file
```shell script
docker run -it --rm --name uminifier -v $PWD:/tmp yeyeto2788/uminifier /tmp/<file_to_convert-py> -k
```