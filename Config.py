import os
from xml.etree import ElementTree as ET

def read_properties_file(file_path):
    properties = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line and line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                properties[key] = value
    return properties

def load_xml_files(directory):
    xml_files = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.xml'):
            file_path = os.path.join(directory, file_name)
            xml_files[file_name] = ET.parse(file_path).getroot()
    return xml_files
