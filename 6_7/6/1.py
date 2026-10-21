# question_1.py
# Compute pi using Trapezoidal, Simpson's 1/3, and Simpson's 3/8 rules

import math

def f(x):
    return 1.0 / (1.0 + x**2)

def trapezoidal(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        res += 2 * f(a + i * h)
    return (h / 2.0) * res

def simpson_13(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            res += 2 * f(a + i * h)
        else:
            res += 4 * f(a + i * h)
    return (h / 3.0) * res

def simpson_38(a, b, n):
    h = (b - a) / n
    res = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            res += 2 * f(a + i * h)
        else:
            res += 3 * f(a + i * h)
    return (3.0 * h / 8.0) * res

def main():
    a, b = 0.0, 1.0
    true_pi = math.pi
    
    # N must be a multiple of 6 for all three methods to work on the same N
    intervals = [6, 12, 24]
    
    print("COMPUTING PI (True Value: 3.141592653589793)")
    print("-" * 105)
    print(f"{'Method':<18} | {'Intervals (N)':<15} | {'Integral':<15} | {'Computed Pi':<18} | {'Absolute Error':<20}")
    print("-" * 105)
    
    for n in intervals:
        # Trapezoidal
        int_trap = trapezoidal(a, b, n)
        pi_trap = 4 * int_trap
        err_trap = abs(true_pi - pi_trap)
        print(f"{'Trapezoidal':<18} | {n:<15} | {int_trap:<15.9f} | {pi_trap:<18.9f} | {err_trap:<20.2e}")
        
        # Simpson's 1/3
        int_s13 = simpson_13(a, b, n)
        pi_s13 = 4 * int_s13
        err_s13 = abs(true_pi - pi_s13)
        print(f"{'Simpson 1/3':<18} | {n:<15} | {int_s13:<15.9f} | {pi_s13:<18.9f} | {err_s13:<20.2e}")
        
        # Simpson's 3/8
        int_s38 = simpson_38(a, b, n)
        pi_s38 = 4 * int_s38
        err_s38 = abs(true_pi - pi_s38)
        print(f"{'Simpson 3/8':<18} | {n:<15} | {int_s38:<15.9f} | {pi_s38:<18.9f} | {err_s38:<20.2e}")
        print("-" * 105)

if __name__ == "__main__":
    main()