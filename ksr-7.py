def invert_array(source_array):
    inverted_array = [[0] * len(source_array) for i in range(len(source_array[0]))]
    for i in range(len(source_array)):
        for j in range(len(source_array[i])):
            inverted_array[j][i] = source_array[i][j]

    return inverted_array

if __name__ == '__main__':
    source_array = [[-1, -2], [3, 4], [5, 6], [7, 8]]
    invert_array(source_array)
