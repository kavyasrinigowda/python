import os
import xml.etree.ElementTree as ET

class Model:
    def __init__(self, xml_files_directory):
        self.xml_files = self.load_xml_files(xml_files_directory)

    def load_xml_files(self, directory):
        xml_files = {}
        for filename in os.listdir(directory):
            if filename.endswith('.xml'):
                file_path = os.path.join(directory, filename)
                xml_files[filename] = ET.parse(file_path).getroot()
        return xml_files
