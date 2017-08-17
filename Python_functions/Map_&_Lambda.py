from math import sqrt
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    return [(int(((1+sqrt(5))**i-(1-sqrt(5))**i)/(2**i*sqrt(5)))) for i in range(n)]
 
