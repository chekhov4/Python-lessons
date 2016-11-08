def write_planets_to_file(source_path, target_path):
    my_solar_system = [['Earth','Sun', 159000000,'km'], ['Naboo', 'Sunaboo', 34, 'light years'], ['some_planet_3', 'some_sun_3', 434, 'parcecs']]
    iterator = 0

    try:
        source_file = open(source_path, 'r')
    except IOError:
        print('Cannot open file')
        return
    try:
        target_file = open(target_path, 'w')
    except IOError:
        print('Cannot create target file')
        return

    read_line = source_file.readline()
    while read_line != '':
        read_line = read_line.replace("{first}",str(my_solar_system[iterator][0]))
        read_line = read_line.replace("{sun}", str(my_solar_system[iterator][1]))
        read_line = read_line.replace("{distance}", str(my_solar_system[iterator][2]))
        read_line = read_line.replace("{units}", str(my_solar_system[iterator][3]))

        iterator += 1
        if iterator == len(my_solar_system):
           iterator = 0
        target_file.writelines(read_line)
        read_line = source_file.readline()

    source_file.close()
    target_file.close()

if __name__ == '__main__':
    source_path ='c:\\temp\\source_planet.txt'
    target_path ='c:\\temp\\target_planet.txt'
    """
    expecting source file like:
    {first} blabla bla {sun} hahaha {distance} he he he {units} us us us
    {first} 2 blabla bla {sun} hahaha {distance} he he he {units} us us us
    """
    write_planets_to_file(source_path, target_path)
