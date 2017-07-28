import os
import unittest
from common_helper_files import get_dir_of_file

from common_helper_passwords import get_merged_password_set

TEST_DATA_DIR = os.path.join(get_dir_of_file(__file__), 'data')


class TestHelperFunctionsPasswords(unittest.TestCase):

    def test_get_merged_password_set(self):
        test_dir = os.path.join(TEST_DATA_DIR, 'password_lists')
        passwords = get_merged_password_set(test_dir)
        self.assertEqual(len(passwords), 3, 'number of passwords not correct')
        self.assertNotIn('', passwords, 'empty password not removed')

    def test_get_merged_password_set_no_blank_lines(self):
        test_dir = os.path.join(TEST_DATA_DIR, 'password_lists/possible_failure')
        passwords = get_merged_password_set(test_dir)
        self.assertEqual(len(passwords), 2, 'number of passwords not correct')
