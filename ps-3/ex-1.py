def f(x):
    return x*(x-1)

def numerical_derivative(func,x,delta):
    return (func(x+delta)-func(x))/delta

for i in range(2,14,2):
    der =  numerical_derivative(f,1,10**(-i))
    print(f"Derivative at x = 1 for delta = 10^-{i} is {der}")

