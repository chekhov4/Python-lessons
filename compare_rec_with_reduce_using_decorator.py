import time

def timer(f):
    def tmp(*args, **kwargs):
        start_time = time.time()

        result = f(*args, **kwargs)

        end_time = time.time()
        print 'execution time {}'.format(end_time - start_time)
        return result
    return tmp

@timer
def get_factorial_rec(value):
    fact_rec = factorial_with_recursion(value)
    print 'fact with recursion',fact_rec

@timer
def get_factorial_reduce(value):
    fact_red = reduce(lambda x, y: x * y, xrange(1, value+1))
    print 'fact with reduce', fact_red

def factorial_with_recursion(factorial):
    if factorial <= 1:
        return 1
    else:
        return factorial*factorial_with_recursion(factorial-1)


if __name__ == '__main__':


    print get_factorial_rec(888)
    print get_factorial_reduce(888)

