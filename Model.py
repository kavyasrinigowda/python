import os
import xml.etree.ElementTree as ET

class Model:
    def __init__(self, application_properties_file, xml_files_directory):
        self.application_properties_file = application_properties_file
        self.xml_files_directory = xml_files_directory
        self.xml_files = self.load_xml_files()

    def load_xml_files(self):
        xml_files = {}
        for filename in os.listdir(self.xml_files_directory):
            if filename.endswith(".xml"):
                file_path = os.path.join(self.xml_files_directory, filename)
                try:
                    tree = ET.parse(file_path)
                    xml_files[filename] = tree.getroot()
                except ET.ParseError:
                    print(f"Error parsing XML file: {file_path}")
        return xml_files

    def get_value_from_xml(self, key):
        for filename, root in self.xml_files.items():
            for elem in root.iter():
                if elem.tag == key:
                    return elem.text
        return None
