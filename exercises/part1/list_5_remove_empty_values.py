raw_values = ["Alice", "", "Bob", "   ", "Chloe", None]


def remove_empty_values(values):
    values_valid = []

    for value in values:
        if isinstance(value, str):
            clean_value = value.strip()
            if clean_value == "":
                continue
            values_valid.append(clean_value)
    return values_valid


print(remove_empty_values(raw_values))        # ["Alice", "Bob", "Chloe"]
print(remove_empty_values([]))                # []
print(remove_empty_values(["", None, "  "]))  # []
