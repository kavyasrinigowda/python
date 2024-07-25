import argparse
from src.utils import load_xml_files, resolve_properties_placeholders, write_processed_properties_file
from src.parser import find_problems

def read_properties_file(properties_file, xml_files):
    # Process the properties file to resolve placeholders
    resolved_key_value_pairs = resolve_properties_placeholders(properties_file, xml_files)
    return resolved_key_value_pairs

def find_and_report_problems(resolved_key_value_pairs):
    # Find problems in the key-value pairs
    problems = find_problems(resolved_key_value_pairs)
    if problems:
        print("Problems found:")
        for problem in problems:
            print(f" - {problem}")
    else:
        print("No problems found")

def main():
    parser = argparse.ArgumentParser(description="Process properties and XML files.")
    parser.add_argument('properties_file', help="Path to the properties file")
    parser.add_argument('xml_files_directory', help="Directory containing XML files")
    parser.add_argument('output_mode', type=int, help="Output mode: 1 for console, 2 for file")

    args = parser.parse_args()

    # Define XML file names dynamically based on the directory
    xml_file_names = [
        'cbc-osb-common.xml',
        'cbc-osb-dev-tire.xml',
        'cbc-osb-dev01.xml',
        'cbc-service-cbc-osb-common.xml',
        'cbc-service-cbc-osb-dev-tire.xml',
        'cbc-service-cbc-osb-dev01.xml'
    ]
    
    xml_file_paths = [f"{args.xml_files_directory}/{name}" for name in xml_file_names]
    
    # Load XML files
    xml_files = load_xml_files(xml_file_paths)
    
    # Read and process properties file
    resolved_key_value_pairs = read_properties_file(args.properties_file, xml_files)
    
    # Find and report problems
    find_and_report_problems(resolved_key_value_pairs)
    
    # Output mode handling
    if args.output_mode == 1:
        for key, value in resolved_key_value_pairs.items():
            print(f"{key}={value}")
    elif args.output_mode == 2:
        output_file = f"{args.properties_file.replace('.properties', '_output.properties')}"
        write_processed_properties_file(output_file, resolved_key_value_pairs)
        print(f"Output written to {output_file}")
    else:
        print("Invalid output mode. Use 1 for console or 2 for file.")

if __name__ == '__main__':
    main()
