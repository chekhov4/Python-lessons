def summ_and_mult(n):

    if n == 0: return (0, 0)
    mutlp = 1
    summa = 0
    to_string = str(n)

    for i in range(len(to_string)):
        summa = summa + int(to_string[i])
        mutlp = mutlp * int(to_string[i])

    return (summa, mutlp)