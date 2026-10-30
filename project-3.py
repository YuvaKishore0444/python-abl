passwords_to_test = ["Pass1", "SecurePass123"]

for pwd in passwords_to_test:
    errors = []

    if len(pwd) < 8:
        errors.append("Must be at least 8 characters long.")

    has_upper = False
    has_lower = False
    has_digit = False

    for char in pwd:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not has_upper:
        errors.append("Missing at least one uppercase letter.")
    if not has_lower:
        errors.append("Missing at least one lowercase letter.")
    if not has_digit:
        errors.append("Missing at least one numeric digit.")

    print(f"\nTesting Password: '{pwd}'")

    if not errors:
        print("Status: VALID PASSWORD")
    else:
        print("Status: INVALID PASSWORD")
        for err in errors:
            print(f" - Error: {err}")