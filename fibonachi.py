def find_fyb_n(n):
    n_0 = 0
    n_1 = 1

    for i in range(2, n+1):
 #      ch = fyb[i-1] + fyb[i-2]  # if neccessary to store all Fibonachi numbers
 #      fyb.append(ch)
        fyb_n = n_0  + n_1
        n_0 = n_1
        n_1 = fyb_n

    return fyb_n
