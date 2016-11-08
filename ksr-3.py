def find_values():
    values = []
    for i in range(100, 701):
        digits_sum = i % 10 + (i % 100 ) // 10 + (i % 1000) // 100
        if digits_sum == 7:
            values.append(i)
    return values

if __name__ == '__main__':
    find_values()

