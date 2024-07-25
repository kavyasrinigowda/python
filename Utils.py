def output_mode(mode, properties):
    if mode == 1:
        # Print to console
        for key, value in properties.items():
            print(f"{key}: {value}")
    elif mode == 2:
        # Write to properties file
        try:
            with open('output_properties.properties', 'w') as f:
                for key, value in properties.items():
                    f.write(f"{key}={value}\n")
        except Exception as e:
            raise Exception(f"Error writing to properties file: {e}")
