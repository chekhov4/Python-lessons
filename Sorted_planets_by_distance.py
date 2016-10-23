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

def sort_solar_planets_by_distance():
     get_planets = solar_system()
     sorted_planets = sorted(get_planets, lambda x, y: cmp(int(get_planets[x]), int(get_planets[y])))
     for key in sorted_planets:
        print('Planet {} is {} km far away from the sun').format(key, get_planets[key])
     return 'printed'

if __name__ == '__main__':

    sort_solar_planets_by_distance()