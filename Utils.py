import os

def output_mode(mode, properties):
    if mode == 1:
        # Print to console
        for key, value in properties.items():
            print(f"{key}={value}")
    elif mode == 2:
        # Output to file
        output_file = 'output_test.properties'
        with open(output_file, 'w') as file:
            for key, value in properties.items():
                file.write(f"{key}={value}\n")
    else:
        raise ValueError("Invalid output mode specified. Use 1 for console or 2 for file.")

def log_missing_properties(missing_properties):
    if missing_properties:
        with open('missing_properties.log', 'w') as file:
            for prop in missing_properties:
                file.write(f"{prop}\n")
