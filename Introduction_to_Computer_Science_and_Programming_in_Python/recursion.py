### Factorial 
##Iteration 
def factorial_Iteration(n):
    result = 1 
    while n > 1:
        result = result * n 
        n -= 1 

    return result 

print(factorial_Iteration(5))

#Recursion 
def factorial_Recursion(n):
    #base case
    if n == 1:
        return n 

    else:
        return n * factorial_Recursion(n-1)

print(factorial_Recursion(5))

#### Fibonacci 
def fib(n):
    if n == 0 or n == 1:
        return 1 

    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of ', i, '= ', fib(i))

testFib(5)

#Palindrome testing
def isPalindrome(s):

    def toChars(s):
        s = s.lower() 
        letters = ''
        for c in s:
            if c.isalpha():
                letters = letters + c
        return letters 

    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

def testPalindrome():
    print("is dogGod palindrome?")
    print(isPalindrome('dogGod'))
    print("is doGood palindrome?")
    print(isPalindrome('doGood'))

testPalindrome()

#global variable
def fib(n):
    global num_calls 
    num_calls += 1 
    if n == 0 or n == 1:
        return 1 
    else:
        return fib(n-1) + fib(n-2)

def testFib_count(n):
    for i in range(n+1):
        global num_calls 
        num_calls = 0 
        print('fib of ', i, '=', fib(i))
        print('fib called ', num_calls, ' times.')  

testFib_count(5)  
