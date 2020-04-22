#Implement Newton's method 
#Newton's method is more efficient than bisection search

#Newton-Raphson for square root 
#Find x such that x**2 - 24 is within epsilon of 0.01

epsilon = 0.01 
k = 24 

#function: x**2 - 24 = 0 
guess = k/2 

while abs(guess**2 - k) >= epsilon:
    guess = guess - (guess**2 - 24)/(2*guess) 

print(f"Square root of {k} is about {guess}")

