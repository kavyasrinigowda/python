def parse_properties_file(properties, xml_files):
    problems = []
    missing_properties = []

    for key, value in properties.items():
        if '$' in value:
            xml_key = value.strip('$')
            xml_value = xml_files.get_value_from_xml(xml_key)
            if xml_value:
                properties[key] = xml_value
            else:
                problems.append(f"Reference {xml_key} not found in XML files")
                missing_properties.append(key)

    return problems, missing_properties
