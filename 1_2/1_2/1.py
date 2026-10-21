# question_1.py
# Solves for sqrt(2) using the Bisection method up to 50 iterations.

def f(x):
    return x**2 - 2

def main():
    # Initial interval [1, 2] since f(1) = -1 and f(2) = 2
    a = 1.0
    b = 2.0
    
    # Table header
    print(f"{'Iteration':<10} | {'a':<12} | {'b':<12} | {'c=(a+b)/2':<12} | {'f(a)':<12} | {'f(b)':<12} | {'f(c)':<12}")
    print("-" * 100)
    
    # Perform iterations from 0 to 50
    for i in range(51):
        c = (a + b) / 2.0
        
        fa = f(a)
        fb = f(b)
        fc = f(c)
        
        # Print current iteration details
        print(f"{i:<10} | {a:<12.9f} | {b:<12.9f} | {c:<12.9f} | {fa:<12.9f} | {fb:<12.9f} | {fc:<12.9f}")
        
        # Update the interval
        if fa * fc < 0:
            b = c
        else:
            a = c

if __name__ == "__main__":
    main()