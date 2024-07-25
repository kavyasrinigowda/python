def parse_properties_file(properties, xml_files):
    problems = []
    missing_properties = []
    new_properties = {}
    
    # Define namespaces if applicable
    namespaces = {'ns': 'http://example.com/namespace'}  # Update with actual namespace if needed

    for filename, root in xml_files.items():
        for prop, value in properties.items():
            element = root.find(f".//*[name()='{prop}']", namespaces)
            if element is not None:
                if element.text.strip() != value:
                    problems.append(f"{prop}: {value} in {filename}")
            else:
                missing_properties.append(f"{prop} not found in {filename}")
                new_properties[prop] = value

    return problems, missing_properties, new_properties
