# Number-Star ladder
def pattern(n):
    
    res = '1'

    for i in range (2, n+1, 1):
        res = res + '\n1' + '*'*(i-1) + str(i)
           
    
    return res 
	
# Sum of Multiples
def sum_mul(n, m):
    if n <= 0 or m <= 0: return 'INVALID'

    if n >= m: return 0
    res = n
    mul = n + n

    while mul < m:
        res = res + mul
        mul += n
    return res

# Jenny's secret message
def greet(name):
  
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# Grasshopper - Summation
def summation(num):
    pass # Code here
    res = 0
    while num > 0:
        res = res + num
        num = num - 1

    return res

#Lario and Muigi Pipe Problem
def pipe_fix(inc_pipe):
    i = 0
    delta = inc_pipe[(len(inc_pipe) - 1)] - inc_pipe[0]
    for i in range(1, delta):
        if inc_pipe[i] <> (inc_pipe[i-1]+1):
            inc_pipe.insert(i, inc_pipe[i-1]+1)
    return inc_pipe
	
# Convert a Boolean to a String
def boolean_to_string(b):
    #your code here
    if b == True:
        return "True"
    else:
        return "False"
		
# Switch/Case - Bug Fixing #6
def eval_object(v):
    return {'+': v['a']+v['b'],
        '-': v['a']-v['b'],
        '/': v['a']/v['b'],
        '*': v['a']*v['b'],
        '%': v['a']%v['b'],
        '**': v['a']**v['b'], }.get(v['operation'],1)

# Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i+=1
    return res
	
# Get Planet Name By ID
def get_planet_name(id):
    # This doesn't work; Fix it!
    return {
        1 : "Mercury",
        2 : "Venus",
        3 : "Earth",
        4 : "Mars",
        5 : "Jupiter",
        6 : "Saturn",
        7 : "Uranus",
        8 : "Neptune"
    }[id]
	
	
# Sum Arrays
def sum_array(a):
    s=0
    for i in range (0, len(a)):
        s = s + a[i]

    return s
	
	
# Fuel Calculator
def fuelPrice(litres, pricePerLiter):
    #your code here
    import math
    
    discount = min( math.trunc(litres / 2) * 0.05, 0.25)
    return round((litres*(pricePerLiter-discount)),2)
    
	
# Sum of positive
def positive_sum(arr):
    # Your code here
    res = 0
    
    if len(arr) < 1:
        return 0
    
    for i in range (len(arr)):
        if arr[i] > 0:
            res = res + arr[i]
    
    return res
	

# No zeros for heros
def no_boring_zeros(n):
    # your code
    import math

    if n == 0:
        return 0


    while  math.fmod(n, 10) == 0:
        n = n / 10


    return n
	
# Points of Reflection
def symmetric_point(p, q):
    # your code here
    import math
    
    delta_x = math.fabs(q[0]-p[0])
    delta_y = math.fabs(q[1]-p[1])
    
    if p[0] <= q[0]:
        p1_x = q[0] + delta_x     
    else:
        p1_x = q[0] - delta_x
    
    if p[1] <= q[1]:
        p1_y = q[1] + delta_y
    else:
        p1_y = q[1] - delta_y
    
    
    return [p1_x, p1_y]
	
	
# Find n'th Digit of a Number
def find_digit(num, nth):
    #your code here
    import math

    if num < 0: 
        num = math.fabs(num)

    if nth <= 0:
        return -1
        
    if num < 10**(nth-1):
        return 0
    

    n = math.fmod(num, 10**nth)
    n = math.trunc(n/(10**(nth-1)))
    
    return n
	

# noobCode 01: SUPERSIZE ME.... or rather, this integer!
def super_size(n):
    #your code here
    import math
    a=[]
    res = 0

    while n > 0:
        a.append(int(math.fmod(n, 10)))
        n = math.trunc(n / 10)

    a.sort(reverse=True)

    for i in range (0, len(a)):
        res = res*10 + a[i]


    return res
	

# Convert number to reversed array of digits
def digitize(n):
    import math
    
    a=[]

    while n > 0:
        a.append(int(math.fmod(n, 10)))
        n = math.trunc(n / 10)

    return a
	
	
# Evil or Odious
def evil(n):
    
    import math
    
    str = bin(n)
    count = 0  
    
    for i in range(2, len(str)):
        if int(str[i]) == 1:
            count += 1
    
    if math.fmod(count ,2 ) == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
		
		
# Count by X
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    
    """
  
    a = []
    
    for y in range (n):
        a.append(x * (y+1))
        
    return a
	
	
	
# Heads and Legs
def animals(heads, legs):
    # return (Chickens, Cows)
    import math

    if legs == 0 and heads == 0:
        return (0, 0)

    if legs < 0 or heads < 0:
        return "No solutions"

    Chickens = heads - (legs - 2 * heads) / 2
    Cows = (legs - 2 * heads) / 2

    if math.fabs(Chickens - math.ceil(Chickens)) > 0  or math.fabs(Cows - math.ceil(Cows)) > 0:
        return  "No solutions"

    if Chickens < 0 or Cows < 0:
        return "No solutions"

  #  print ('Chickens', Chickens, 'Cows', Cows)

    return (Chickens, Cows)
	
	
# 