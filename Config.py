import os
import xml.etree.ElementTree as ET

def read_properties_file(file_path):
    properties = {}
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                properties[key] = value
    return properties

def load_xml_files(directory):
    xml_files = {}
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory, filename)
            xml_files[filename] = ET.parse(file_path).getroot()
    return xml_files
