import unittest
from xml.etree import ElementTree as ET
from src.interpreter import load_xml_files, find_differences_in_xml
import os

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        # Define the test XML file paths
        self.test_data_dir = 'src/test/test_data'
        self.xml_files = {
            'cbc-osb-common.xml': os.path.join(self.test_data_dir, 'cbc-osb-common.xml'),
            'cbc-osb-dev-tire.xml': os.path.join(self.test_data_dir, 'cbc-osb-dev-tire.xml'),
            'cbc-osb-dev01.xml': os.path.join(self.test_data_dir, 'cbc-osb-dev01.xml'),
            'cbc-service-cbc-osb-common.xml': os.path.join(self.test_data_dir, 'cbc-service-cbc-osb-common.xml'),
            'cbc-service-cbc-osb-dev-tire.xml': os.path.join(self.test_data_dir, 'cbc-service-cbc-osb-dev-tire.xml'),
            'cbc-service-cbc-osb-dev01.xml': os.path.join(self.test_data_dir, 'cbc-service-cbc-osb-dev01.xml')
        }
        # Load the XML files
        self.xml_files_content = load_xml_files(self.xml_files.values())
        
        # Prepare mock XML content
        for path, root in self.xml_files_content.items():
            child = ET.SubElement(root, "item")
            name = ET.SubElement(child, "name")
            name.text = "key"
            value = ET.SubElement(child, "value")
            value.text = "value"

    def test_find_differences_in_xml(self):
        key = 'key'
        differences = find_differences_in_xml(self.xml_files_content, key)
        self.assertGreater(len(differences), 0)

if __name__ == '__main__':
    unittest.main()
