import xml.etree.ElementTree as ET

class Model:
    def __init__(self, application_properties_file, xml_files_directory):
        self.application_properties_file = application_properties_file
        self.xml_files = self._load_xml_files(xml_files_directory)

    def _load_xml_files(self, directory_path):
        xml_files = {}
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.xml'):
                tree = ET.parse(os.path.join(directory_path, file_name))
                xml_files[file_name] = tree.getroot()
        return xml_files
