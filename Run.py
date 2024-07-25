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
        problems, missing_properties = parse_properties_file(combined_properties, model)

        # Debug output
        print("Combined properties:", combined_properties)
        print("Problems:", problems)
        print("Missing properties:", missing_properties)

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
    except Exception as e:
        print(f"Problem 4: Output logic error - {e}")
