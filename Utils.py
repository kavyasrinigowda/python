import os

def output_mode(mode, properties):
    """
    Handle the output based on the mode.
    
    Mode 1: Print to console
    Mode 2: Write to properties file
    
    Args:
        mode (int): Output mode (1 or 2)
        properties (dict): Key-value pairs to output
    """
    if mode == 1:
        # Print properties to the console
        for key, value in properties.items():
            print(f"{key}={value}")
    elif mode == 2:
        # Write properties to a file
        output_file = 'output_properties.properties'
        with open(output_file, 'w') as file:
            for key, value in properties.items():
                file.write(f"{key}={value}\n")
        print(f"Properties written to {output_file}")
    else:
        raise ValueError("Invalid output mode. Use 1 for console or 2 for file.")

def log_missing_properties(missing_properties):
    """
    Log missing properties to a file.
    
    Args:
        missing_properties (list): List of missing properties
    """
    if missing_properties:
        log_file = 'missing_properties.log'
        with open(log_file, 'w') as file:
            for prop in missing_properties:
                file.write(f"Missing property: {prop}\n")
        print(f"Missing properties logged to {log_file}")
