import xml.etree.ElementTree as ET

def load_xml_files(file_paths):
    xml_files = {}
    for file_path in file_paths:
        try:
            tree = ET.parse(file_path)
            xml_files[file_path] = tree.getroot()
        except Exception as e:
            print(f"Error loading XML file {file_path}: {e}")
    return xml_files

def get_value_from_xml(name, xml_files):
    for xml_root in xml_files.values():
        element = xml_root.find(f".//*[name='{name}']")
        if element is not None:
            return element.find('value').text
    return None

def process_properties_file(properties_file, xml_files):
    with open(properties_file, 'r') as file:
        lines = file.readlines()
    
    processed_lines = []
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            if '${' in value:
                placeholder = value.strip().strip('${').strip('}')
                xml_value = get_value_from_xml(placeholder, xml_files)
                if xml_value:
                    value = xml_value
                else:
                    print(f"Warning: Placeholder '{placeholder}' not found in XML files")
            processed_lines.append(f"{key}={value}")
        else:
            processed_lines.append(line)
    
    return processed_lines

def write_processed_properties_file(properties_file, processed_lines):
    with open(properties_file, 'w') as file:
        file.writelines(processed_lines)
