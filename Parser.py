import xml.etree.ElementTree as ET
import os

def parse_properties_file(properties, xml_files):
    problems = []
    missing_properties = []

    try:
        for key, value in properties.items():
            # Check if the value contains a reference to an XML property
            if value.startswith('$'):
                xml_property = value[1:]  # Remove the '$' prefix
                if not any(xml_property in xml_file for xml_file in xml_files):
                    problems.append(f"Reference '{xml_property}' not found in any XML file.")
                    missing_properties.append(key)
    except FileNotFoundError as e:
        problems.append(f"Problem 1: File not found - {e}")
    except ET.ParseError as e:
        problems.append(f"Problem 2: Parsing error - {e}")
    except KeyError as e:
        problems.append(f"Problem 3: Missing reference - {e}")
    except Exception as e:
        problems.append(f"Problem 4: Output logic error - {e}")

    return problems, missing_properties                   
    
