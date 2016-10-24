def create_random_array(n, m, make_random):
    import random
    if make_random == True:
        random_array = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                random_array[i][j] = random.randint(-2, 2)

        return random_array
    else:
        return [[2,7,6],[9,5,1],[4,3,8]]
def check_unique_values_in_array(get_array):

    all_values = []

    for i in range(len(get_array)):
        for j in range(len(get_array)):
            all_values.append(get_array[i][j])

    for i in range(len(all_values)):
        if all_values.count(all_values[i]) > 1:
            return False

    return True

def check_magic_square():
    get_square = create_random_array(3, 3, False)

    if check_unique_values_in_array(get_square) == False:
        return 'no magic in the square. not unique items'

    magic_number = len(get_square)*(len(get_square)**2 + 1) / 2
    temp_sum_row = 0
    temp_sum_col = 0
    sum_diagonal = 0
    for i in range(len(get_square)):
        for j in range(len(get_square)):
            temp_sum_row += get_square[i][j]
            temp_sum_col += get_square[j][i]
        if temp_sum_row != magic_number:
            return 'no magic in the square. wrong sum in row'
        elif temp_sum_col != magic_number:
            return 'no magic in square. wrong sum in column'
        else:
            temp_sum_row = 0
            temp_sum_col = 0
        sum_diagonal += get_square[i][i]
    if sum_diagonal != magic_number:
        return 'no magic in the square. wrong diagonal sum'
    else:
        return 'Holy magic in the square!!!'


if __name__ == '__main__':

    print check_magic_square()
