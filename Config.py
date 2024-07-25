import os

def read_properties_file(file_path):
    properties = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties

def load_xml_files(directory_path):
    xml_files = {}
    for file_name in os.listdir(directory_path):
        if file_name.endswith('.xml'):
            xml_files[file_name] = os.path.join(directory_path, file_name)
    return xml_files
