def parse_properties_file(properties, xml_files):
    problems = []
    for key, value in properties.items():
        if value.startswith('${'):
            ref_key = value[2:-1]  # Extract the key within ${}
            found = False
            for xml_name, xml_root in xml_files.items():
                element = xml_root.find(f".//*[name='{ref_key}']")
                if element is not None:
                    value = element.find('value').text
                    properties[key] = value
                    found = True
                    break
            if not found:
                problems.append(f"Key '{key}' references non-existent XML value '{ref_key}'")
    return problems
