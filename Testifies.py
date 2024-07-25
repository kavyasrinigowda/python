import unittest
from src.utils import output_mode_console, output_mode_file

class TestUtils(unittest.TestCase):
    def test_output_mode_console(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        output_mode_console(data)  # This should print to console

    def test_output_mode_file(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        output_mode_file(data, 'src/test/test_data/output_test.properties')
        with open('src/test/test_data/output_test.properties', 'r') as file:
            lines = file.readlines()
        self.assertIn('key1 = value1\n', lines)
        self.assertIn('key2 = value2\n', lines)

if __name__ == '__main__':
    unittest.main()
