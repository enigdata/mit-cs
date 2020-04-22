#Approximation Solutions and Bisection Search 

#Example: fine the square root of 25
#Approximation using exhaustive enumeration 
x = 25
epsilon = 0.01 
step = epsilon ** 2 
numGuesses = 0 
ans = 0 
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step 
    numGuesses += 1 
print('numGuesses = ', numGuesses)
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of", x)
else:
    print(ans, 'is close to square root of', x)

#Approximation using bisection search 
#x = 25 
x = 0.8
epsilon = 0.01 
numGuesses = 0 
low = 0 
high = max(1, x)

ans = (high + low) / 2 
while abs(ans ** 2 - x) >= epsilon:
    print('low ', low, ' high ', high, ' ans ', ans)
    numGuesses += 1 
    if ans**2 < x: 
        low = ans 
    else:
        high = ans 
    ans = (high + low)/2
print('number of guesses are ', numGuesses)
print(ans, 'is close to the square root of ', x)
