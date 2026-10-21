# question_2.py
# Fixed Point Iteration Method for two equations

import math

def g_a(x):
    # Rewriting x^3 - x - 1 = 0 as x = (x + 1)^(1/3)
    return (x + 1.0) ** (1.0 / 3.0)

def g_b(x):
    # Equation is x = (2 - e^x + x^2) / 3
    return (2.0 - math.exp(x) + x**2) / 3.0

def fixed_point(g_func, x0, tol=1e-7, max_iter=500):
    x_old = x0
    for i in range(1, max_iter + 1):
        x_new = g_func(x_old)
        if abs(x_new - x_old) < tol:
            return x_new, i
        x_old = x_new
    return x_old, max_iter

def main():
    print("FIXED POINT ITERATION METHOD")
    
    # 2(a) x^3 - x - 1 = 0 in [1, 2]
    # Starting guess x0 = 1.5 (midpoint)
    x0_a = 1.5
    root_a, steps_a = fixed_point(g_a, x0_a)
    print("\nEquation 2(a): x^3 - x - 1 = 0 in [1, 2]")
    print(f"Initial Guess: {x0_a}")
    print(f"Approximate Root: {root_a:.9f}")
    print(f"Iterations (Accuracy < 1e-7): {steps_a}")

    # 2(b) x = (2 - e^x + x^2) / 3
    # Starting guess x0 = 0.5 (midpoint of [0, 1])
    x0_b = 0.5
    root_b, steps_b = fixed_point(g_b, x0_b)
    print("\nEquation 2(b): x = (2 - e^x + x^2) / 3")
    print(f"Initial Guess: {x0_b}")
    print(f"Approximate Root: {root_b:.9f}")
    print(f"Iterations (Accuracy < 1e-7): {steps_b}")

if __name__ == "__main__":
    main()