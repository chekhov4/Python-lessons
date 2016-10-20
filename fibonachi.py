def biggest_mult(n):
    fyb = [0,1]

    for i in range(2, n):
       ch = fyb[i-1] + fyb[i-2]
       fyb.append(ch)

    print (fyb[n])
    return fyb[n]

biggest_mult(7)
