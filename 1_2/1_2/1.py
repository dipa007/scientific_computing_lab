def f(x):
    return x**2 - 2

def main():
    a = 1.0
    b = 2.0
    
    print(f"{'Iteration':<10} | {'a':<12} | {'b':<12} | {'c=(a+b)/2':<12} | {'f(a)':<12} | {'f(b)':<12} | {'f(c)':<12}")
    print("-" * 100)
    
    for i in range(51):
        c = (a + b) / 2.0
        fa = f(a)
        fb = f(b)
        fc = f(c)
        
        print(f"{i:<10} | {a:<12.9f} | {b:<12.9f} | {c:<12.9f} | {fa:<12.9f} | {fb:<12.9f} | {fc:<12.9f}")
        
        if fa * fc < 0:
            b = c
        else:
            a = c

if __name__ == "__main__":
    main()