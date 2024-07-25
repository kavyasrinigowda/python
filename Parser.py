def parse_properties_file(properties, xml_files):
    problems = []
    missing_properties = []
    new_properties = {}

    for key, value in properties.items():
        if '$' in value:
            xml_value = None
            for xml_file in xml_files.values():
                xml_value = xml_file.findtext(value.strip('$'))
                if xml_value:
                    break

            if xml_value:
                properties[key] = xml_value
            else:
                problems.append(f"Missing value for key '{key}' in XML files")
                missing_properties.append(key)
        else:
            new_properties[key] = value
    
    return properties, missing_properties, new_properties
