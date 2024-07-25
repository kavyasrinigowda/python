import argparse
import os
import xml.etree.ElementTree as ET
from src.config import read_properties_file, load_xml_files
from src.parser import parse_properties_file
from src.utils import log_missing_properties
from src.model import Model

def main(application_properties_file, environment_properties_file, xml_files_directory):
    try:
        # Read properties from files
        application_properties = read_properties_file(application_properties_file)
        environment_properties = read_properties_file(environment_properties_file)

        # Initialize the model
        model = Model(application_properties_file, xml_files_directory)

        # Combine properties
        combined_properties = {**environment_properties, **application_properties}

        # Load XML files
        xml_files = load_xml_files(xml_files_directory)

        # Parse properties file and get problems
        problems, missing_properties = parse_properties_file(combined_properties, xml_files)

        # Check and print problems
        if problems:
            print("Problems found:")
            for problem in problems:
                print(f" - {problem}")
            log_missing_properties(missing_properties)
        else:
            print("No problems found.")
    
    except Exception as e:
        print(f"Problem 4: Output logic error - {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process properties and XML files.")
    parser.add_argument('application_properties_file', type=str, help='Path to the application properties file')
    parser.add_argument('environment_properties_file', type=str, help='Path to the environment properties file')
    parser.add_argument('xml_files_directory', type=str, help='Directory containing XML files')
    
    args = parser.parse_args()
    main(args.application_properties_file, args.environment_properties_file, args.xml_files_directory)
