# question_4.py
# Secant and Regula-Falsi methods for f(x) = cos(x) - x*e^x.

import math

def f(x):
    return math.cos(x) - x * math.exp(x)

def secant_method(a_init, b_init, criterion, tol=5e-8, max_iter=500):
    x0, x1 = a_init, b_init
    
    for i in range(1, max_iter + 1):
        # Calculate new point using secant formula
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        
        abs_err = abs(x_new - x1)
        rel_err = abs_err / abs(x_new) if x_new != 0 else abs_err
        func_val = abs(f(x_new))
        
        if criterion == "Absolute Error" and abs_err < tol:
            return a_init, b_init, x_new, i
        elif criterion == "Relative Error" and rel_err < tol:
            return a_init, b_init, x_new, i
        elif criterion == "Functional value" and func_val < tol:
            return a_init, b_init, x_new, i
            
        x0, x1 = x1, x_new
        
    return a_init, b_init, x1, max_iter

def regula_falsi_method(a_init, b_init, criterion, tol=5e-8, max_iter=500):
    a = a_init
    b = b_init
    c_old = None
    
    for i in range(1, max_iter + 1):
        # Calculate new point using false position formula
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        
        if c_old is not None:
            abs_err = abs(c - c_old)
            rel_err = abs_err / abs(c) if c != 0 else abs_err
            func_val = abs(f(c))
            
            if criterion == "Absolute Error" and abs_err < tol:
                return a_init, b_init, c, i
            elif criterion == "Relative Error" and rel_err < tol:
                return a_init, b_init, c, i
            elif criterion == "Functional value" and func_val < tol:
                return a_init, b_init, c, i
                
        # Update interval
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        c_old = c
        
    return a_init, b_init, c_old, max_iter

def main():
    a, b = 0.0, 1.0
    criteria = ["Absolute Error", "Relative Error", "Functional value"]
    
    print("SECANT METHOD")
    print(f"{'Criterion':<20} | {'a':<5} | {'b':<5} | {'Approximate root':<20} | {'No of Iterations':<15}")
    print("-" * 80)
    for crit in criteria:
        a_val, b_val, root, iters = secant_method(a, b, crit)
        print(f"{crit:<20} | {a_val:<5.1f} | {b_val:<5.1f} | {root:<20.9f} | {iters:<15}")
        
    print("\nREGULA-FALSI (FALSE POSITION) METHOD")
    print(f"{'Criterion':<20} | {'a':<5} | {'b':<5} | {'Approximate root':<20} | {'No of Iterations':<15}")
    print("-" * 80)
    for crit in criteria:
        a_val, b_val, root, iters = regula_falsi_method(a, b, crit)
        print(f"{crit:<20} | {a_val:<5.1f} | {b_val:<5.1f} | {root:<20.9f} | {iters:<15}")

if __name__ == "__main__":
    main()