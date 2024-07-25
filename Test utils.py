import unittest
from src.utils import output_mode, log_missing_properties

class TestUtils(unittest.TestCase):
    def test_output_mode_console(self):
        properties = {'key1': 'value1'}
        output_mode(1, properties)  # Should print to console

    def test_output_mode_file(self):
        properties = {'key1': 'value1'}
        output_mode(2, properties)  # Should write to 'output_test.properties'

    def test_log_missing_properties(self):
        missing_properties = ['key2 not found in file.xml']
        log_missing_properties(missing_properties)  # Should write
