def sum_and_mult(n):
    multp = 1
    summa = 0
    if n == 0: return (0 ,0)

    while n // 10 > 0:

        n1 = n % 10
        summa = summa + n1
        multp = multp * n1
        n = n // 10

    n1 = n % 10
    summa = summa + n1
    multp = multp * n1


    return (summa, multp)
