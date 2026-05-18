names = [" alice ", "BOB", " ChLoE "]


def normalize_names(names):
    normalized_names = []
    for name in names:
        name_clean = name.strip().capitalize()
        normalized_names.append(name_clean)
    return normalized_names

print(normalize_names(names))  # ["Alice", "Bob", "Chloe"]
print(normalize_names([]))     # []
