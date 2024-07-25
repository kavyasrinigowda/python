import os
from xml.etree import ElementTree as ET

def load_xml_files(file_paths):
    xml_files = {}
    for file_path in file_paths:
        if os.path.exists(file_path):
            xml_files[file_path] = ET.parse(file_path).getroot()
        else:
            print(f"Warning: {file_path} does not exist")
    return xml_files

def resolve_properties_placeholders(properties_file, xml_files):
    resolved_pairs = {}
    with open(properties_file, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                resolved_pairs[key] = resolve_value(value, xml_files)
    return resolved_pairs

def resolve_value(value, xml_files):
    if '${' in value:
        parts = value.split('${')
        resolved_value = parts[0]
        for part in parts[1:]:
            key, remainder = part.split('}', 1)
            resolved_value += resolve_key_from_xml(key, xml_files) + remainder
        return resolved_value
    return value

def resolve_key_from_xml(key, xml_files):
    for xml_root in xml_files.values():
        element = xml_root.find(f".//*[@name='{key}']")
        if element is not None:
            return element.find('value').text
    return key  # Return the key if not found in any XML

def write_processed_properties_file(file_path, key_value_pairs):
    with open(file_path, 'w') as f:
        for key, value in key_value_pairs.items():
            f.write(f"{key}={value}\n")
