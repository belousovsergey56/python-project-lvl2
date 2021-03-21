"""Contains functions for creating and describing the console utility."""
import argparse
from sys import stdout

from differences.kernel import (read_file, gendiff)


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
    file_path_one = read_file.read_json_file(args.first_file)
    file_path_two = read_file.read_json_file(args.second_file)
    stdout.write(gendiff.generate_diff(file_path_one, file_path_two))


if __name__ == '__main__':
    main()
