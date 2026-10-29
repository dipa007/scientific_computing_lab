import math

def f(x):
    return math.exp(-x / 5.0) - math.sin(x)

def secant(x0, x1, tol=1e-7, max_iter=500):
    for i in range(1, max_iter + 1):
        if abs(f(x1) - f(x0)) == 0:
            break
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if abs(f(x_new)) < tol:
            return x_new, i
        x0, x1 = x1, x_new
    return x1, max_iter

def regula_falsi(a, b, tol=1e-7, max_iter=500):
    if f(a) * f(b) >= 0:
        return None, 0
    for i in range(1, max_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c, i
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, max_iter

def main():
    intervals = [(0.5, 1.5), (2.0, 3.0), (6.0, 7.1), (8.8, 9.8)]
    
    print("SECANT METHOD")
    print(f"{'Interval [x0, x1]':<20} | {'Approx Root':<15} | {'|f(root)|':<15} | {'Steps'}")
    print("-" * 65)
    for a, b in intervals:
        root, steps = secant(a, b)
        print(f"[{a:<3.1f}, {b:<4.1f}]{'':<9} | {root:<15.9f} | {abs(f(root)):<15.2e} | {steps}")
    print("\nREGULA FALSI METHOD")
    print(f"{'Interval [a, b]':<20} | {'Approx Root':<15} | {'|f(root)|':<15} | {'Steps'}")
    print("-" * 65)
    for a, b in intervals:
        root, steps = regula_falsi(a, b)
        print(f"[{a:<3.1f}, {b:<4.1f}]{'':<9} | {root:<15.9f} | {abs(f(root)):<15.2e} | {steps}")

if __name__ == "__main__":
    main()