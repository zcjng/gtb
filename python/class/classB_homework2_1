x = input()

try:
    # Try integer first
    n = int(x)
    # Make sure input was really an integer (not "3.0")
    if '.' not in x:
        print(f"{n:05d}")
    else:
        raise ValueError  # force float formatting

except ValueError:
    try:
        n = float(x)
        before, after = x.split('.')  # split input into integer and decimal parts
        total_digits = len(before) + len(after)

        if total_digits >= 5:
            # Just print with 4 decimals
            print(f"{n:.4f}")
        else:
            # Need to pad decimals so that total = 5
            needed = 5 - len(before)
            print(f"{n:.{needed}f}")

    except ValueError:
        print("not a number")
