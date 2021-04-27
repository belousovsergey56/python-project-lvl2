"""Values for test."""
from differences.kernel.engine import difference_to_list, sorting_to_list
from differences.kernel.read_file import read_json_file

result_difference2list = [
    {'-': {'follow': False}},
    {' ': {'host': 'hexlet.io'}},
    {'-': {'proxy': '123.234.53.22'}},
    {'-': {'timeout': 50}},
    {'+': {'timeout': 20}},
    {'+': {'verbose': True}},
]

file_one = read_json_file('differences/tests/fixtures/file_1.json')
file_two = read_json_file('differences/tests/fixtures/file_2.json')
remove = list(file_one.keys() - file_two.keys())
add = list(file_two.keys() - file_one.keys())
unchanged = list(file_one.keys() & file_two.keys())
sort_list = sorting_to_list(remove, add, unchanged)
diff_list = difference_to_list(file_one, file_two, add, remove, sort_list)
