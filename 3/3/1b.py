# question_1b.py
# Bisection Method for f(x) = e^(-x/5) - sin(x) = 0

import math

def f(x):
    return math.exp(-x / 5.0) - math.sin(x)

def bisection(a, b, tol=1e-7, max_iter=500):
    if f(a) * f(b) >= 0:
        return None, 0
        
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        if abs(f(c)) < tol:
            return c, i
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
    return c, max_iter

def main():
    intervals = [(0.5, 1.5), (2.0, 3.0), (6.0, 7.1), (8.8, 9.8)]
    
    print(f"{'Interval [a, b]':<20} | {'Approx Root':<15} | {'|f(root)|':<15} | {'Steps'}")
    print("-" * 65)
    
    for a, b in intervals:
        root, steps = bisection(a, b)
        if root is not None:
            print(f"[{a:<3.1f}, {b:<4.1f}]{'':<9} | {root:<15.9f} | {abs(f(root)):<15.2e} | {steps}")
        else:
            print(f"[{a:<3.1f}, {b:<4.1f}] -> Invalid interval")

if __name__ == "__main__":
    main()