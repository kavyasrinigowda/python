import argparse
from src.config import read_properties_file
from src.parser import parse_properties_file
from src.utils import output_mode_console, output_mode_file

def main():
    parser = argparse.ArgumentParser(description='Process properties and XML files.')
    parser.add_argument('app_properties', help='Path to the application properties file')
    parser.add_argument('env_properties', help='Path to the environment properties file')
    parser.add_argument('output_mode', type=int, choices=[1, 2], help='Output mode: 1 for console, 2 for file')
    parser.add_argument('output_file', help='Path to the output file (required if output_mode is 2)')

    args = parser.parse_args()

    # Read properties files
    app_properties = read_properties_file(args.app_properties)
    env_properties = read_properties_file(args.env_properties)

    # Parse properties and find problems
    problems = parse_properties_file(app_properties)
    if problems:
        print("Problems found:")
        for problem in problems:
            print(problem)
        return 1  # Indicate error due to problems

    # Determine output mode
    output_data = {**app_properties, **env_properties}
    if args.output_mode == 1:
        output_mode_console(output_data)
    elif args.output_mode == 2:
        if args.output_file:
            output_mode_file(output_data, args.output_file)
        else:
            print("Output file path is required when output mode is 2")
            return 1  # Indicate error due to missing file path

    return 0  # Indicate success

if __name__ == '__main__':
    exit(main())
