def f(x):
    """Function to integrate."""
    return x**4 - 2*x + 1

def trapezoidal_rule(func, a, b, N):
    """Compute the integral of func from a to b using the trapezoidal rule with N slices."""
    h = (b - a) / N
    integral = 0.5 * func(a) + 0.5 * func(b)
    
    for i in range(1, N):
        integral += func(a + i * h)
    
    return integral * h

I_1 = trapezoidal_rule(f, 0, 2, 10)
I_2 = trapezoidal_rule(f, 0, 2, 20)


epsilon = (1/3) * (I_2 - I_1)

# Direct computation of the error with respect to the true value
direct_error = abs(I_2 - 4.4)

print(I_2,epsilon,direct_error)
