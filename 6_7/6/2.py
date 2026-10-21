# question_2.py
# Simpson's 1/3 rule with a target error < 0.5 * 10^-5

import math

def f(x):
    return 1.0 / (1.0 + x**2)

def simpson_13(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            res += 2 * f(a + i * h)
        else:
            res += 4 * f(a + i * h)
    return (h / 3.0) * res

def main():
    a, b = 0.0, 1.0
    true_val = math.pi / 4.0
    target_error = 0.5 * 1e-5
    
    n = 2 # Smallest number of intervals for Simpson 1/3
    
    print(f"Target Error Tolerance: {target_error}")
    print("-" * 65)
    print(f"{'Sub-intervals (N)':<20} | {'Approx Integral':<20} | {'Absolute Error':<20}")
    print("-" * 65)
    
    while True:
        approx = simpson_13(a, b, n)
        error = abs(true_val - approx)
        
        print(f"{n:<20} | {approx:<20.9f} | {error:<20.2e}")
        
        if error < target_error:
            print("-" * 65)
            print(f"Target accuracy reached at N = {n}")
            break
            
        n += 2 # Must remain even for Simpson's 1/3

if __name__ == "__main__":
    main()