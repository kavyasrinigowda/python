import unittest
from xml.etree import ElementTree as ET
from src.interpreter import load_xml_files, find_differences_in_xml

class TestInterpreter(unittest.TestCase):
    def setUp(self):
        self.xml_files = {
            'src/test/test_data/cbc-osb-common.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'src/test/test_data/cbc-osb-dev-tire.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'src/test/test_data/cbc-osb-dev01.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'src/test/test_data/cbc-service-cbc-osb-common.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'src/test/test_data/cbc-service-cbc-osb-dev-tire.xml': ET.ElementTree(ET.Element("root")).getroot(),
            'src/test/test_data/cbc-service-cbc-osb-dev01.xml': ET.ElementTree(ET.Element("root")).getroot()
        }
        for file in self.xml_files:
            root = self.xml_files[file]
            child = ET.SubElement(root, "item")
            name = ET.SubElement(child, "name")
            name.text = "key"
            value = ET.SubElement(child, "value")
            value.text = "value"

    def test_find_differences_in_xml(self):
        key = 'key'
        differences = find_differences_in_xml(self.xml_files, key)
        self.assertGreater(len(differences), 0)

if __name__ == '__main__':
    unittest.main()
