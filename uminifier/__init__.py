#!/usr/bin/env python3
"""Minification script for saving memory for Micropython use.

```
usage: compilation_test.py [-h] [-o OUTPUT] [-k] [-v] filename

Convert python files into .mpy (Micropython) files.

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output path or output filename.
  -k, --keep            Keep any intermediate file generated.
  -v, --verbose         Print verbose output.
```

Modules needed installation:
```shell
pip install pyminifier>=2.1 mpy-cross>=1.12
```
"""
__version__ = "0.1.0"
__author__ = "Juan Biondi"
__email__ = "juanernestobiondi@gmail.com"

import argparse
import os
import sys

import mpy_cross
from pyminifier import minification
from pyminifier import token_utils


class PyminiferOptions:
    """Class to define the options used for the pyminifier module."""

    def __init__(self):
        """Constructor to define the properties for minification."""
        # Use tabs instead of spaces
        self.tabs = False
        # Obfuscate all code
        self.obfuscate = False
        self.obf_classes = False
        self.obf_functions = False

        self.nominify = False
        self.obf_variables = False
        self.obf_builtins = False
        self.obf_import_methods = False
        self.replacement_length = 1
        self.use_nonlatin = False


class TColors:
    header = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def get_file_size(file_path) -> int:
    """Get the file size in bytes.

    Args:
        file_path:

    Returns: File size in bytes

    """
    return os.stat(file_path).st_size


def minify_code(file_path) -> str:
    """Function to minify the code of a given python file.

    Args:
        file_path:

    Returns: Minified code.

    """
    # Open the file and read it's content.
    with open(file_path, 'r') as f:
        source = f.read()

    # Get tokens from file.
    tokens = token_utils.listified_tokenizer(source)
    # Minify the file content based on the tokens
    minified = minification.minify(tokens, PyminiferOptions())
    # Recompute tokens from minified version.
    tokens = token_utils.listified_tokenizer(minified)
    # Final result on file minified.
    result = token_utils.untokenize(tokens)

    return result


def uminify(arguments) -> None:
    """Main logic for converting a given file into .mpy file format

    Check for file existance and execute the minification of the code within the file
    and convert it into `.mpy` file format using `mpy-cross` library.

    Args:
        arguments:

    Returns:
        None

    Raises:
        ValueError: When filename does not exists.
    """

    def log_it(*args, **kwargs):
        """Wrapper function in order to print verbose output.

        Args:
            *args: Arguments to be passed to the print function.
            **kwargs: Keyword Arguments to be passed to the print function.

        Returns:
            None
        """
        if arguments.verbose:
            print(*args, flush=True, **kwargs)

    input_file = os.path.abspath(arguments.filename)
    intermediate_filename = os.path.join(
        os.path.dirname(os.path.abspath(arguments.filename)),
        f"i{os.path.basename(os.path.abspath(arguments.filename))}"
    )
    output_file = os.path.abspath(arguments.output)
    output_dir = os.path.dirname(os.path.abspath(output_file))

    if not os.path.exists(input_file):
        raise ValueError(f"Seems like the path {input_file} do not exists.")

    # Get input_file size.
    input_size = get_file_size(input_file)
    log_it(f"{input_file}: {input_size} B")

    # Minify the code.
    result = minify_code(input_file)
    # Check whether the output directory exists if not create it.
    if not os.path.exists(output_dir):
        log_it(f"Creating {output_dir} directory.")
        os.makedirs(output_dir, exist_ok=True)

    # Write minified content to a intermediate file.
    with open(intermediate_filename, 'w') as inter_file:
        inter_file.write(result)

    # Get the file size of the generated intermediate file.
    intermediate_size = get_file_size(intermediate_filename)
    log_it(f"{intermediate_filename}: {intermediate_size} B")

    # Convert Python code into mpy byte code.
    compilation_execution = mpy_cross.run(
        "-o",
        output_file,
        intermediate_filename
    )
    # Wait for the process to be finished.
    compilation_execution.wait()

    # Get the output_file size.
    output_size = get_file_size(output_file)
    log_it(f"{output_file}: {output_size} B")

    # Remove intermediate file created if everything when Ok.
    if not compilation_execution.returncode and os.path.exists(
            intermediate_filename):

        if not arguments.keep:
            log_it(f"Deleting {intermediate_filename}")
            os.remove(intermediate_filename)

    log_it(
        f"\n{TColors.bold + TColors.okgreen}{input_size - output_size} "
        f"Bytes reduced.{TColors.endc}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Convert python files into .mpy (Micropython) files.",
        epilog="Report any bug at https://github.com/yeyeto2788/uminifier/issues"
    )
    parser.add_argument(
        "-o",
        "--output",
        action='store',
        default='',
        help='Output path or output filename.'
    )
    parser.add_argument(
        "-k",
        "--keep",
        action='store_const',
        default=False,
        const=True,
        help="Keep any intermediate file generated."
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action='store_const',
        default=False,
        const=True,
        help="Print verbose output."
    )
    parser.add_argument('filename')

    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)

    args = parser.parse_args()

    if args.output == '':
        args.output = args.filename.replace('.py', '.mpy')

    try:
        uminify(args)

    except ValueError as exec_error:
        print(f"{TColors.fail}{exec_error}{TColors.endc}")
        print(f"{TColors.warning}{str(args)}{TColors.endc}")
        exit(-1)

    else:
        print(f"\n{TColors.okgreen}Execution successful.{TColors.endc}")


if __name__ == '__main__':
    main()
