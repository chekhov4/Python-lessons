def simple(m):
    for i in range(2, m):
        if m % i == 0:
            return 'False'

    return 'True'


def biggest_mult(n):
    mnozhiteli = []

    for i in range(2, n + 1):

        if n % i == 0 and simple(i) == 'True':
            mnozhiteli.append(i)
            biggest_dev = i

    return (mnozhiteli, biggest_dev)