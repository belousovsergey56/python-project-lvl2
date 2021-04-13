"""Test modules kernel package."""
import pytest

from differences.kernel.engine import kernel_differences, multiple_replace
from differences.kernel.read_file import read_json_file


@pytest.mark.parametrize('string_line, answer', [
    ("PATH::/'bin'/{'myscript'", 'PATH:/bin/myscript'),
    (":'host': {}'hexlet.io'", 'host: hexlet.io'),
    ("pr':oxy': {'123.234.53.22'}'", 'proxy: 123.234.53.22')
])
def test_multiple_replace(string_line, answer):
    """Test function."""
    replace_values = {'{': '', '}': '', ':': '', "'": ''}
    assert multiple_replace(string_line, replace_values) == answer
