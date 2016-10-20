def solar_system():
    dictionary = {
        "Mercury": 57000000,
        "Venus": 108000000,
        "Earth": 150000000,
        "Mars": 227000000,
        "Jupiter": 778000000,
        "Saturn": 1427000000,
        "Uranus": 2871000000,
        "Neptune": 4497000000
        }
    return dictionary

def print_solar_system():
     to_print = solar_system()
     for keys, values in to_print.items():
         print('Planet {} is {} km far away from the sun').format(keys, values)


if __name__ == '__main__':