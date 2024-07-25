import unittest
from src.utils import output_mode_console, output_mode_file
import os

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Define data for testing
        self.data = {'key1': 'value1', 'key2': 'value2'}
        self.output_file_path = 'src/test/test_data/output_test.properties'

    def test_output_mode_console(self):
        output_mode_console(self.data)  # This will print to the console

    def test_output_mode_file(self):
        output_mode_file(self.data, self.output_file_path)
        with open(self.output_file_path, 'r') as file:
            lines = file.readlines()
        self.assertIn('key1=value1\n', lines)
        self.assertIn('key2=value2\n', lines)
        os.remove(self.output_file_path)  # Clean up the output file after test

if __name__ == '__main__':
    unittest.main()
