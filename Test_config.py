import unittest
from src.config import read_properties_file, load_xml_files

class TestConfig(unittest.TestCase):
    def test_read_properties_file(self):
        properties = read_properties_file('src/test/test_data/application.properties')
        self.assertIn('key1', properties)
        self.assertEqual(properties['key1'], 'value1')

    def test_load_xml_files(self):
        xml_files = load_xml_files('src/test/test_data/')
        self.assertGreater(len(xml_files), 0)  # Ensure at least one XML file is loaded

if __name__ == '__main__':
    unittest.main()
