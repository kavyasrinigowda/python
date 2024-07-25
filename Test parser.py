import unittest
from src.parser import parse_properties_file
from src.config import load_xml_files

class TestParser(unittest.TestCase):

    def setUp(self):
        self.xml_files = load_xml_files('src/test/test_data')

    def test_parse_properties_file(self):
        properties = {'key1': '${reference1}', 'key2': 'value2'}
        problems, missing_properties = parse_properties_file(properties, self.xml_files)
        self.assertIn('Key \'key1\' references non-existent XML value \'reference1\'', problems)
        self.assertEqual(missing_properties['key1'], '${reference1}')

if __name__ == '__main__':
    unittest.main()
