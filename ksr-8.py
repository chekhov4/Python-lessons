def find_biggest_in_array(source_array):
    all_values = []

    def expand(source_array):
        for i in range(len(source_array)):
            if type(source_array[i]) == list:
                expand(source_array[i])
            else:
                all_values.append(source_array[i])

    expand(source_array)

    all_values = sorted(all_values, reverse=  True)
    return all_values[0]


if __name__ == '__main__':
    source_array = [[[2,-7,-6],[-9,-5,-1],[-4,-3,-8]],[[-2,3000,-6],[-9,-5,-1],[-4,-3,-8]]]
    find_biggest_in_array(source_array)
