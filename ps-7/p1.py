import numpy as np
from scipy.optimize import minimize_scalar
def f(x):
    return (x - 0.3)**2 * np.exp(x)
def brent_minimize(f, a, b, tol=1e-5, max_iter=100):
    golden_ratio = (3 - 5**0.5) / 2  # About 0.618

    # Define initial points
    v = w = x = a + golden_ratio * (b - a)
    fv = fw = fx = f(x)
    d = e = b - a

    for _ in range(max_iter):
        m = 0.5 * (a + b)
        tol1 = tol * abs(x) + tol / 10
        tol2 = 2 * tol1

        # Check if the tolerance is met
        if abs(x - m) <= tol2 - 0.5 * (b - a):
            return x, f(x)

        p = q = r = 0.0
        if abs(e) > tol1:
            # Fit parabola
            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2 * (q - r)
            if q > 0:
                p = -p
            q = abs(q)
            r = e
            e = d

        if abs(p) < abs(0.5 * q * r) and p > q * (a - x) and p < q * (b - x):
            # Parabolic interpolation step
            d = p / q
            u = x + d

            # f must not be evaluated too close to a or b
            if (u - a) < tol2 or (b - u) < tol2:
                d = tol1 if x < m else -tol1
        else:
            # Golden-section step
            e = a - x if x >= m else b - x
            d = golden_ratio * e

        # f must not be evaluated too close to x
        u = x + d if abs(d) >= tol1 else x + np.sign(d) * tol1
        fu = f(u)

        if fu <= fx:
            if u >= x:
                a = x
            else:
                b = x
            v, w, x = w, x, u
            fv, fw, fx = fw, fx, fu
        else:
            if u < x:
                a = u
            else:
                b = u
            if fu <= fw or w == x:
                v, w = w, u
                fv, fw = fw, fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu

    return x, f(x)

custom_brent_result = brent_minimize(f, 0, 1)
scipy_brent_result = minimize_scalar(f, bracket=(0, 1), method='brent')

print(custom_brent_result)
print(scipy_brent_result)