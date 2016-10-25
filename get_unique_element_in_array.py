def create_random_array(n, m):
    import random
    random_array = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            random_array[i][j] = random.randint(-2, 2)

    return random_array

def get_uniue_values_from_array(n, m):

    get_array = create_random_array(n, m)
    all_values = []
    unique_values = []
    print(get_array)
    for i in range(n):
        for j in range(m):
            all_values.append(get_array[i][j])

    for i in range(len(all_values)):
        if all_values.count(all_values[i]) == 1:
            unique_values.append(all_values[i])

    print (unique_values)
    return unique_values

if __name__ == '__main__':

    get_uniue_values_from_array(3,3)