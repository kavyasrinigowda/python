import os  # Ensure os module is imported

def output_mode(mode, properties):
    if mode == 1:
        # Print to console
        for key, value in properties.items():
            print(f"{key}: {value}")
    elif mode == 2:
        # Output to file
        output_file_path = os.path.join('src', 'test', 'test_data', 'output_test.properties')
        with open(output_file_path, 'w') as file:
            for key, value in properties.items():
                file.write(f"{key}={value}\n")

def log_missing_properties(missing_properties):
    log_file_path = os.path.join('src', 'test', 'test_data', 'missing_properties.log')
    with open(log_file_path, 'w') as file:
        for prop in missing_properties:
            file.write(f"Missing property: {prop}\n")
