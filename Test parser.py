import unittest
from src.parser import parse_properties_file

class TestParser(unittest.TestCase):
    def test_parse_properties_file(self):
        properties = {'key1': '${value1', 'key2': 'value2'}
        problems = parse_properties_file(properties)
        self.assertGreater(len(problems), 0)

if __name__ == '__main__':
    unittest.main()
