import os
from xml.etree import ElementTree as ET

class Model:
    def __init__(self, properties_file, xml_files_directory):
        self.properties = self.load_properties(properties_file)
        self.xml_files = self.load_xml_files(xml_files_directory)
    
    def load_properties(self, file_path):
        properties = {}
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line and line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    properties[key] = value
        return properties
    
    def load_xml_files(self, directory):
        xml_files = {}
        for file_name in os.listdir(directory):
            if file_name.endswith('.xml'):
                file_path = os.path.join(directory, file_name)
                xml_files[file_name] = ET.parse(file_path).getroot()
        return xml_files
