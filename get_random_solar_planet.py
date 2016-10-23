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

def get_random_solar_planet():
     import random
     get_planets = solar_system()
     random_key = random.choice(get_planets.keys())
     print('Planet {} is {} km far away from the sun').format(random_key, get_planets[random_key])
     return 'printed'

if __name__ == '__main__':

    get_random_solar_planet()