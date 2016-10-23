def create_random_array(n, m):
    import random
    random_array = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            random_array[i][j] = random.randint(-100, 100)

    return random_array

def negative_array_values_arith_mean(n, m):

    get_array = create_random_array(n, m)
    total_negative_summ = 0
    negative_count = 0
    for i in range(n):
        for j in range(m):
            if get_array[i][j] < 0:
                total_negative_summ += get_array[i][j]
                negative_count +=1
    if negative_count == 0:
        print ('no negative values in array. Arithmetical is 0')
    else:
        print ('Naegative values arthmetical mean is ', total_negative_summ / negative_count )

    print (get_array)

if __name__ == '__main__':

    negative_array_values_arith_mean(2,3) 