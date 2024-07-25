import os

def output_mode(mode, properties):
    if mode == 1:
        for key, value in properties.items():
            print(f"{key}={value}")
    elif mode == 2:
        output_file = 'output.properties'
        with open(output_file, 'w') as file:
            for key, value in properties.items():
                file.write(f"{key}={value}\n")

def log_missing_properties(missing_properties):
    with open('missing_properties.txt', 'w') as file:
        for prop in missing_properties:
            file.write(f"{prop}\n")
