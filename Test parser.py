import unittest
from src.parser import parse_properties_file

class TestParser(unittest.TestCase):
    def setUp(self):
        # Define properties for testing
        self.properties = {
            'key1': '${value1',
            'key2': 'value2'
        }

    def test_parse_properties_file(self):
        problems = parse_properties_file(self.properties)
        self.assertGreater(len(problems), 0)

if __name__ == '__main__':
    unittest.main()
