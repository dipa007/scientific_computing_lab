# question_3.py
# Newton-Raphson and Fixed-Point Iteration for f(x) = cos(x) - x*e^x.

import math

def f(x):
    return math.cos(x) - x * math.exp(x)

def df(x):
    return -math.sin(x) - math.exp(x) * (1 + x)

def g(x):
    return math.cos(x) * math.exp(-x)

def newton_raphson(a, b, x0, criterion, tol=5e-8, max_iter=500):
    x_old = x0
    for i in range(1, max_iter + 1):
        x_new = x_old - f(x_old) / df(x_old)
        
        abs_err = abs(x_new - x_old)
        rel_err = abs_err / abs(x_new) if x_new != 0 else abs_err
        func_val = abs(f(x_new))
        
        if criterion == "Absolute Error" and abs_err < tol:
            return a, b, x0, x_new, i
        elif criterion == "Relative Error" and rel_err < tol:
            return a, b, x0, x_new, i
        elif criterion == "Functional value" and func_val < tol:
            return a, b, x0, x_new, i
            
        x_old = x_new
    return a, b, x0, x_old, max_iter

def fixed_point(a, b, x0, criterion, tol=5e-8, max_iter=500):
    x_old = x0
    for i in range(1, max_iter + 1):
        x_new = g(x_old)
        
        abs_err = abs(x_new - x_old)
        rel_err = abs_err / abs(x_new) if x_new != 0 else abs_err
        func_val = abs(f(x_new))
        
        if criterion == "Absolute Error" and abs_err < tol:
            return a, b, x0, x_new, i
        elif criterion == "Relative Error" and rel_err < tol:
            return a, b, x0, x_new, i
        elif criterion == "Functional value" and func_val < tol:
            return a, b, x0, x_new, i
            
        x_old = x_new
    return a, b, x0, x_old, max_iter

def main():
    a, b = 0.0, 1.0
    x0 = (a + b) / 2.0
    criteria = ["Absolute Error", "Relative Error", "Functional value"]
    
    print("NEWTON-RAPHSON METHOD")
    print(f"{'Criterion':<18} | {'a':<3} | {'b':<3} | {'x0':<4} | {'Approximate root':<20} | {'No of Iterations':<15}")
    print("-" * 80)
    for crit in criteria:
        a_val, b_val, x0_val, root, iters = newton_raphson(a, b, x0, crit)
        print(f"{crit:<18} | {a_val:<3.1f} | {b_val:<3.1f} | {x0_val:<4.1f} | {root:<20.9f} | {iters:<15}")
        
    print("\nFIXED POINT ITERATION METHOD")
    print(f"{'Criterion':<18} | {'a':<3} | {'b':<3} | {'x0':<4} | {'Approximate root':<20} | {'No of Iterations':<15}")
    print("-" * 80)
    for crit in criteria:
        a_val, b_val, x0_val, root, iters = fixed_point(a, b, x0, crit)
        print(f"{crit:<18} | {a_val:<3.1f} | {b_val:<3.1f} | {x0_val:<4.1f} | {root:<20.9f} | {iters:<15}")

if __name__ == "__main__":
    main()