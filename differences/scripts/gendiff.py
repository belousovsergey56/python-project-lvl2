"""Contains functions for creating and describing the console utility."""
import argparse
from sys import stdout

from differences.kernel.engine import kernel_differences
from differences.kernel.read_file import read_json_file


def generate_diff(path_one, path_two):
    """To reuse the kernel as a library.

    Args:
        path_one: file template
        path_two: new file

    Returns:
        str
    """
    file_one = read_json_file(path_one)
    file_two = read_json_file(path_two)
    return kernel_differences(file_one, file_two)


def main():
    """Use the function to display help.

    Step one.
    The function is designed to give the user a description
    of how to use the utility

    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='positional arguments')
    parser.add_argument('second_file', type=str, help='positional arguments')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    stdout.write(diff)


if __name__ == '__main__':
    main()
