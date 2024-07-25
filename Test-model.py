import unittest
from src.model import get_key_value_pairs

class TestModel(unittest.TestCase):
    def test_get_key_value_pairs(self):
        properties = {'key1': 'value1', 'key2': 'value2'}
        key_value_pairs = get_key_value_pairs(properties)
        self.assertEqual(key_value_pairs['key1'], 'value1')
        self.assertEqual(key_value_pairs['key2'], 'value2')

if __name__ == '__main__':
    unittest.main()
