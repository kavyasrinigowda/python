import argparse
from src.utils import load_xml_files, process_properties_file, write_processed_properties_file
from src.parser import find_problems  # Assuming this function is defined in parser.py

def read_properties_file(properties_file, xml_files):
    # Process the properties file to resolve placeholders
    processed_lines = process_properties_file(properties_file, xml_files)
    return processed_lines

def find_and_report_problems(processed_lines):
    # Find problems in the processed lines
    problems = find_problems(processed_lines)
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
    processed_lines = read_properties_file(args.properties_file, xml_files)
    
    # Find and report problems
    find_and_report_problems(processed_lines)
    
    # Output mode handling
    if args.output_mode == 1:
        for line in processed_lines:
            print(line, end='')
    elif args.output_mode == 2:
        output_file = f"{args.properties_file.replace('.properties', '_output.properties')}"
        write_processed_properties_file(output_file, processed_lines)
        print(f"Output written to {output_file}")
    else:
        print("Invalid output mode. Use 1 for console or 2 for file.")

if __name__ == '__main__':
    main()
