import os

def read_properties_file(file_path):
    properties = {}
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Properties file not found: {file_path}")
    
    with open(file_path, 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                properties[key.strip()] = value.strip()
    return properties

def load_xml_files(directory):
    xml_files = {}
    for filename in os.listdir(directory):
        if filename.endswith('.xml'):
            file_path = os.path.join(directory, filename)
            try:
                tree = ET.parse(file_path)
                xml_files[filename] = tree.getroot()
            except ET.ParseError as e:
                print(f"Error parsing {filename}: {e}")
    return xml_files
