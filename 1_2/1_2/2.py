import math

def f(x):
    return math.cos(x) - x * math.exp(x)

def bisection_method(a_init, b_init, criterion, tol=5e-8, max_iter=500):
    a = a_init
    b = b_init
    c_old = None
    
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
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
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c_old = c
    return a_init, b_init, c_old, max_iter

def main():
    a, b = 0.0, 1.0
    criteria = ["Absolute Error", "Relative Error", "Functional value"]
    
    print(f"{'Criterion':<20} | {'a':<5} | {'b':<5} | {'Approximate root':<20} | {'No of Iterations':<15}")
    print("-" * 80)
    
    for crit in criteria:
        a_val, b_val, root, iters = bisection_method(a, b, crit)
        print(f"{crit:<20} | {a_val:<5.1f} | {b_val:<5.1f} | {root:<20.9f} | {iters:<15}")

if __name__ == "__main__":
    main()