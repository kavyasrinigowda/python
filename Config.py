import os
from xml.etree import ElementTree as ET

def read_properties_file(file_path):
    properties = {}
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line and line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                properties[key] = value
    return properties

def load_xml_files(directory):
    xml_files = {}
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")
    for file_name in os.listdir(directory):
        if file_name.endswith('.xml'):
            file_path = os.path.join(directory, file_name)
            try:
                xml_files[file_name] = ET.parse(file_path).getroot()
            except ET.ParseError as e:
                raise ET.ParseError(f"Error parsing XML file {file_name}: {e}")
    return xml_files
