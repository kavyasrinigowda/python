import unittest
from src.config import read_properties_file

class TestConfig(unittest.TestCase):
    def test_read_properties_file(self):
        properties = read_properties_file('src/test/test_data/sample.properties')
        self.assertEqual(properties['key1'], 'value1')
        self.assertEqual(properties['key2'], 'value2')

if __name__ == '__main__':
    unittest.main()
