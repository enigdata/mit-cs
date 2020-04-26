#### Two versions of bisection search implementation

# Version 1
def bisection_search1(L, e):
    if L == []:
        return False 

    elif len(L) == 1:
        return L[0] == e 

    else:
        half = len(L)//2 

        if L[half] > e:
            return bisection_search1(L[:half], e)

        else:
            return bisection_search1(L[half:], e)

#O(log(n)) bisection search calls 
#O(n) for each bisection call to copy list 
#The time complexity is O(n * log(n))

#Version 2 
def bisection_search2(L, e):

    def search_helper(L, e, low, high):
        if high == low:
            return L[low] == e 

        mid = (high + low) // 2 
        if L[mid] == e:
            return True 

        elif L[mid] > e:
            return bisection_search2(L, e, low, mid - 1)
        else:
            return bisection_search2(L, e, mid+1, high)

#O(log(n)) bisection search calls 
# constance runtime within each recursion call 
# Therefore the time complexity is O(log(n))

##### Logarithmic complexity 

def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'

    res = ''
    while i > 0:
        res = digits[i%10] + res 
        i = i//10 
    return res 

# O(log(i))

####### Factorial Example
# O(n) for iterative factorial 
# 
def fact_iter(n):
    prod = 1 
    for i in range(1, n+1):
        prod *= i 

    return prod

#Still O(n) for recursive factorial because the number of function calls is linear in n
# and constant effort to set up the recursion call 
# 
def fact_recur(n):
    if n <= 1:
        return 1 
    else:
        return n * fact_recur(n-1)

###### Power Set: exponential complexity 
def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]

    smaller = genSubsets(L[:-1]) # all subsets without the last element 
    extra = L[-1:] #list of just last element 
    new = [] 
    for small in smaller:
        new.append(small + extra) # for all smaller solutions, add one with last element 

    return smaller + new 

# for a set of size k there are 2**k cases, and therefore the time complexity is exponential  

####### Fibonacci example

#Iterative Fibonacci
#O(n)
def fib_iter(n):
    if n==0:
        return 0
    elif n==1:
        return 1 

    else:
        fib_1 = 0 
        fib_2 = 1 
        for i in range(n-1):
            temp = fib_1
            fib_1 = fib_2
            fib_2 = temp + fib_1

        return fib_2 

#Recursive Finbonacci

def fib_recur(n):
    if n==0:
        return 0 
    elif n == 1:
        return 1

    else:
        return fib_recur(n-1) + fib_recur(n-2)

#O(2**n)

