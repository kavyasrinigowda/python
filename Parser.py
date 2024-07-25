def find_problems(key_value_pairs):
    problems = []
    for key, value in key_value_pairs.items():
        if not key or not value:
            problems.append(f"Invalid key-value pair: {key}={value}")
        # Add more specific problem checks as needed
    return problems
