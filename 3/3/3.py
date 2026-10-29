import math

def g_a(x):
    return (x + 1.0) ** (1.0 / 3.0)

def g_b(x):
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
    print("VARYING INITIAL GUESS (x0) FOR FIXED POINT ITERATION")
    print("\nEquation 2(a): x = (x + 1)^(1/3)")
    print(f"{'Initial Guess (x0)':<20} | {'Approx Root':<15} | {'Iterations'}")
    print("-" * 55)
    for x0 in [1.0, 1.25, 1.75, 2.0]:
        root, steps = fixed_point(g_a, x0)
        print(f"{x0:<20.2f} | {root:<15.9f} | {steps}")
    print("\nEquation 2(b): x = (2 - e^x + x^2) / 3")
    print(f"{'Initial Guess (x0)':<20} | {'Approx Root':<15} | {'Iterations'}")
    print("-" * 55)
    for x0 in [0.0, 0.25, 0.75, 1.0]:
        root, steps = fixed_point(g_b, x0)
        print(f"{x0:<20.2f} | {root:<15.9f} | {steps}")

if __name__ == "__main__":
    main()