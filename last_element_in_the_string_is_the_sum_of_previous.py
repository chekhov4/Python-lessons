def create_random_array(n, m):
    import random
    random_array = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            random_array[i][j] = random.randint(-1, 4)

    return random_array

def get_uniue_values_from_array(n, m):

    get_array = create_random_array(n, m)
    all_values = []
    summ = 0
    
    for i in range(len(get_array)):       # detecting size of M
        for j in range(len(get_array[i])-1): # detecting size on N
            summ += get_array[i][j]
        get_array[i][j+1] = summ
        summ = 0

    print(get_array)

if __name__ == '__main__':

    get_uniue_values_from_array(3,3)