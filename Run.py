import argparse
import os
import xml.etree.ElementTree as ET
from src.config import read_properties_file, load_xml_files
from src.parser import parse_properties_file
from src.utils import output_mode, log_missing_properties
from src.model import Model

def main(application_properties_file, environment_properties_file, xml_files_directory, output_mode_value):
    try:
        # Read properties from files
        application_properties = read_properties_file(application_properties_file)
        environment_properties = read_properties_file(environment_properties_file)

        # Initialize the model
        model = Model(application_properties_file, xml_files_directory)

        # Combine properties
        combined_properties = {**environment_properties, **application_properties}

        # Parse properties file and get problems
        problems, missing_properties = parse_properties_file(combined_properties, model.xml_files)

        # Check and print problems
        if problems:
            print("Problems found:")
            for problem in problems:
                print(f" - {problem}")
            log_missing_properties(missing_properties)
        else:
            print("No problems found.")

        # Output results based on mode
        output_mode(output_mode_value, combined_properties)
    
    except FileNotFoundError as e:
        print(f"Problem 1: File not found - {e}")
    except ET.ParseError as e:
        print(f"Problem 2: Parsing error - {e}")
    except KeyError as e:
        print(f"Problem 3: Missing reference - {e}")
    except OSError as e:
        print(f"Problem 4: Output logic error related to OS - {e}")
    except Exception as e:
        print(f"Problem 5: General error - {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process properties and XML files.")
    parser.add_argument('application_properties_file', type=str, help='Path to the application properties file')
    parser.add_argument('environment_properties_file', type=str, help='Path to the environment properties file')
    parser.add_argument('xml_files_directory', type=str, help='Directory containing XML files')
    parser.add_argument('output_mode', type=int, choices=[1, 2], help='Output mode: 1 for console, 2 for file')
    
    args = parser.parse_args()
    main(args.application_properties_file, args.environment_properties_file, args.xml_files_directory, args.output_mode)
