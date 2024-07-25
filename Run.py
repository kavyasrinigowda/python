import argparse
from src.config import read_properties_file
from src.parser import parse_properties_file
from src.utils import output_mode_console, output_mode_file

def main(properties_file_path, xml_files_dir, output_mode):
    # Read properties file
    properties = read_properties_file(properties_file_path)

    # Parse properties file and find problems
    problems = parse_properties_file(properties)
    
    if len(problems) > 0:
        print("Problems found:")
        for problem in problems:
            print(problem)
    else:
        print("No problems found.")

    # Output results based on mode
    if output_mode == 1:
        output_mode_console(properties)
    elif output_mode == 2:
        output_mode_file(properties, 'src/test/test_data/output_test.properties')
    else:
        print("Invalid output mode specified.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the property file analysis.")
    parser.add_argument("properties_file", help="Path to the properties file")
    parser.add_argument("xml_files_dir", help="Directory containing XML files")
    parser.add_argument("output_mode", type=int, choices=[1, 2], help="Output mode: 1 for console, 2 for file")
    
    args = parser.parse_args()
    main(args.properties_file, args.xml_files_dir, args.output_mode)
