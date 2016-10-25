def create_random_array(n, m, make_random):
    import random
    if make_random == True:
        random_array = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                random_array[i][j] = random.randint(-2, 2)
        return random_array
    else:
        return [[[2,-7,-6],[-9,-5,-1],[-4,-3,-8]],[[-2,-7,-6],[-9,-5,-1],[-4,-3,-8]]]


def check_unique_values_in_array():
    get_array = create_random_array(0, 0, make_random=False)
    all_values = []
    unique_values = []
    def expand(expand_array):
        for i in range(len(expand_array)):
            if type(expand_array[i]) == list:
                expand(expand_array[i])
            else:
                all_values.append(expand_array[i])

    expand(get_array)

    for i in range(len(all_values)):
        if all_values.count(all_values[i]) == 1:
            unique_values.append(all_values[i])

    if len(unique_values) > 0:
        return 'Unique values in array are', unique_values
    else:
        return 'No unique values in array'

if __name__ == '__main__':

    print check_unique_values_in_array()
