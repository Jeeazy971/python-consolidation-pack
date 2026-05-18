temperatures = [18.5, None, 22.0, "hot", 19.5, -5, 30]


def get_valid_temperatures(temperatures):
    temperatures_valid = []
    
    for temperature in temperatures:
        if isinstance(temperature, (int, float)):
            temperatures_valid.append(temperature)
    return temperatures_valid


print(get_valid_temperatures(temperatures))    # [18.5, 22.0, 19.5, -5, 30]
print(get_valid_temperatures([]))              # []
print(get_valid_temperatures([None, "cold"]))  # []
