def make_array_sum_zero(source_array):
    delta = 0
    for item in source_array:
        delta = delta + item

    if delta != 0:
        source_array.append(delta * -1)
    return source_array


if __name__ == '__main__':
    source_array = [-1, -2, 100, 0, 5, 6, 0]
    make_array_sum_zero(source_array)
