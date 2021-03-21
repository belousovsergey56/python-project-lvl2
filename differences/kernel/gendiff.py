"""Module with the function of comparison of two files."""

SIGN_REMOVE = '-'
SIGN_ADDED = '+'
SIGN_UNCHANGED = ' '
last_tmp = '{0}\n  {1}{2}\n'


def multiple_replace(target_str, replace_values) -> str:
    """
    Replace the substituted value.

    Get the replaceable: substituted from the dictionary in the loop
    change all target_str to the substitutable

    Args:
        target_str: str
        replace_values: dict

    Returns:
        str

    """
    for target, new_char in replace_values.items():
        if target == ':':
            target_str = target_str.replace(target, new_char, 1)
        else:
            target_str = target_str.replace(target, new_char)
    return target_str


def diff_result_to_string(sort_list: list) -> str:
    """Convert the input data of the argument to a string.

    Args:
        sort_list: list

    Returns:
        str

    """
    result_string = '\n  '
    replace_values = {'{': '', '}': '', ':': '', "'": ''}
    sort_list = list(map(str, sort_list))
    temporary_list = []
    for values_list in sort_list:
        temporary_list.append(multiple_replace(values_list, replace_values))
    result_string = result_string.join(temporary_list)
    return last_tmp.format('{', result_string, '\n}')


def the_keys_are_in_the_template(template: dict, new_file: dict) -> list:
    """Get the keys that are in the template.

    is_in_two_files = list(new_file.keys() - template.keys())

    Arguments:
        template: dict
        new_file: dict

    Returns:
        list
    """
    return list(new_file.keys() - template.keys())


def there_are_no_keys_in_the_template(template: dict, new_file: dict) -> list:
    """Get keys that are not in the template.

    not_in_the_template = list(template.keys() - new_file.keys())

    Arguments:
        template: dict
        new_file: dict

    Returns:
        list
    """
    return list(template.keys() - new_file.keys())


def the_keys_are_in_both_files(template: dict, new_file: dict) -> list:
    """Get the keys that are in both files.

    is_in_two_files = list(template.keys() & new_file.keys())

    Arguments:
        template: dict
        new_file: dict

    Returns:
        list
    """
    return list(template.keys() & new_file.keys())


def sorting_to_list(*args) -> list:
    """Sort values into a list.

    Uses the sort function, returns sorted list of values

    Args:
        args: list

    Returns:
        list

    """
    list1, list2, list3 = args

    return sorted(list1 + list2 + list3)


def difference_to_list(template, new_file, add, remove, sorted_list) -> list:
    """Use the function to get a list of differences between files.

    The function in the loop bypasses the list of sorted keys,
    compares with the keys from the set and adds to the dictionary
    with the desired indexer, the dictionary is added to the list.

    Arguments:
        template: dict
        new_file: dict
        add: list
        remove: list
        sorted_list: list

    Returns:
        list

    """
    diff_result = []

    for keys_values in sorted_list:
        if keys_values in remove:
            diff_result.append(
                {SIGN_REMOVE: {keys_values: template.get(keys_values)}},
            )
        elif keys_values in add:
            diff_result.append(
                {SIGN_ADDED: {keys_values: new_file.get(keys_values)}},
            )
        elif template.get(keys_values) == new_file.get(keys_values):
            diff_result.append(
                {SIGN_UNCHANGED: {keys_values: template.get(keys_values)}},
            )
        else:
            diff_result.append(
                {SIGN_REMOVE: {keys_values: template.get(keys_values)}},
            )
            diff_result.append(
                {SIGN_ADDED: {keys_values: new_file.get(keys_values)}},
            )
    return diff_result


def generate_diff(template, new_file) -> str:
    """Run methods in module generate_diff.

    Args:
        template: dict
        new_file: dict

    Returns:
        str
    """
    remove = there_are_no_keys_in_the_template(template, new_file)
    add = the_keys_are_in_the_template(template, new_file)
    unchanged = the_keys_are_in_both_files(template, new_file)
    sort_list = sorting_to_list(remove, add, unchanged)
    diff_list = difference_to_list(template, new_file, add, remove, sort_list)

    return diff_result_to_string(diff_list)
