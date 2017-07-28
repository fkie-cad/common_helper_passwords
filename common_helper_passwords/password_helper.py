'''
password helper functions
'''
from common_helper_files.fail_safe_file_operations import get_files_in_dir, get_string_list_from_file
from contextlib import suppress


def get_merged_password_set(directory):
    """
    merges password lists in directory to a set of passwords
    """
    passwords = set()
    password_files = get_files_in_dir(directory)
    for item in password_files:
        passwords.update(get_string_list_from_file(item))
    with suppress(KeyError):
        passwords.remove("")
    return passwords
