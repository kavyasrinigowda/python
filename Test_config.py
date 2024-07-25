import unittest
from src.config import read_properties_file, load_xml_files

class TestConfig(unittest.TestCase):

    def test_read_properties_file(self):
        properties = read_properties_file('src/test/test_data/sample.properties')
        self.assertEqual(properties['key1'], 'value1')
        self.assertEqual(properties['key2'], 'value2')

    def test_load_xml_files(self):
        xml_files = load_xml_files('src/test/test_data')
        self.assertIn('sample.xml', xml_files)

if __name__ == '__main__':
    unittest.main()
