"""Test modules kernel package."""
import pytest
from differences.kernel.engine import (
    diff_result_to_string,
    kernel_differences,
    multiple_replace,
)
from differences.kernel.read_file import read_json_file
from differences.tests.fixtures.result_to_string_test import (
    first_answer,
    first_validator,
    second_answer,
    second_validator,
    third_answer,
    third_validator,
)


def test_engine():
    """Test function kernel_diff, contains two json files."""
    file_one = read_json_file('differences/tests/fixtures/file_1.json')
    file_two = read_json_file('differences/tests/fixtures/file_2.json')
    with open('differences/tests/fixtures/file_output.txt', 'r') as output:
        assert kernel_differences(file_one, file_two) == output.read()


@pytest.mark.parametrize(
    'string_line, answer', [
        ("PATH::/'bin'/{'myscript'", 'PATH:/bin/myscript'),
        ("':host': }'h{exlet.io'", 'host: hexlet.io'),
        ("pr':oxy': {'123.234.53.22'}'", 'proxy: 123.234.53.22'),
    ])
def test_multiple_replace(string_line, answer):
    """Test multi replace signs in string line.

    Example, string line = 'Hel:lo world: okay'
    execute multiple_replace(string_line, replace_value)
    correct_answer is 'Hello world: okay'

    Args:
        string_line: accepted line
        answer: the correct line after the execution of the function
    """
    replace_values = {'{': '', '}': '', ':': '', "'": ''}
    assert multiple_replace(string_line, replace_values) == answer


@pytest.mark.parametrize(
    'sorted_list, answers',
    [(first_validator, first_answer), (second_validator, second_answer),
     (third_validator, third_answer),
     ])
def test_diff_result_to_string(sorted_list, answers):
    """Test function differences result to string.

    Function takes a list of values and returns result as block
        {
            first values
            second values

        }

    Args:
        sorted_list: sorted list of values
        answers: the correct line after the execution of the function
    """
    assert diff_result_to_string(sorted_list) == answers
