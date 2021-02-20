"""Contains functions for creating and describing the console utility."""
import argparse
from sys import stdout


def main():
    """Use the function to display help.

    Step one.
    The function is designed to give the user a description
    of how to use the utility

    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, help='positional arguments')
    parser.add_argument('second_file', type=str, help='positional arguments')
    args = parser.parse_args()
    stdout.write(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
