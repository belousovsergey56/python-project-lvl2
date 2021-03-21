"""The module implements the functions of opening and reading files."""
import json
from os import path


def read_json_file(file_path):
    """Read json file.

    Args:
        file_path: json file

    Returns:
        dict
    """
    path_file = ''.join(path.splitext(file_path))

    with open(path_file, 'r') as json_file:
        return json.load(json_file)
