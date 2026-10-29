import math

def f(x):
    return math.exp(-x / 5.0) - math.sin(x)

def df(x):
    return -0.2 * math.exp(-x / 5.0) - math.cos(x)

def ddf(x):
    return 0.04 * math.exp(-x / 5.0) + math.sin(x)

def newton(x0, tol=1e-7, max_iter=500):
    x = x0
    for i in range(1, max_iter + 1):
        if abs(f(x)) < tol:
            return x, i - 1
        x = x - f(x) / df(x)
    return x, max_iter

def chebyshev(x0, tol=1e-7, max_iter=500):
    x = x0
    for i in range(1, max_iter + 1):
        if abs(f(x)) < tol:
            return x, i - 1
        fx = f(x)
        dfx = df(x)
        ddfx = ddf(x)
        x = x - (fx / dfx) - 0.5 * (fx**2 * ddfx) / (dfx**3)
    return x, max_iter

def main():
    intervals = [(0.5, 1.5), (2.0, 3.0), (6.0, 7.1), (8.8, 9.8)]
    starting_points = [(a + b) / 2.0 for a, b in intervals]
    
    print("NEWTON'S METHOD")
    print(f"{'Initial Point x0':<20} | {'Approx Root':<15} | {'|f(root)|':<15} | {'Steps'}")
    print("-" * 65)
    for x0 in starting_points:
        root, steps = newton(x0)
        print(f"{x0:<20.4f} | {root:<15.9f} | {abs(f(root)):<15.2e} | {steps}")
    print("\nCHEBYSHEV METHOD")
    print(f"{'Initial Point x0':<20} | {'Approx Root':<15} | {'|f(root)|':<15} | {'Steps'}")
    print("-" * 65)
    for x0 in starting_points:
        root, steps = chebyshev(x0)
        print(f"{x0:<20.4f} | {root:<15.9f} | {abs(f(root)):<15.2e} | {steps}")

if __name__ == "__main__":
    main()