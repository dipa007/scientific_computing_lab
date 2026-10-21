# question_4.py
# RK2 Methods for y' = x(y - x) at various step lengths

import matplotlib.pyplot as plt

def f(x, y):
    return x * (y - x)

def exact_rk4_baseline(x_target):
    x, y, h = 2.0, 3.0, 1e-5
    while x < x_target - h/2:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x += h
    return y

def rk2_solve(x0, y0, h, x_end, method):
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_n, y_n = x_vals[-1], y_vals[-1]
        k1 = f(x_n, y_n)
        
        if method == "Midpoint":
            k2 = f(x_n + h/2.0, y_n + (h/2.0) * k1)
            y_next = y_n + h * k2
        elif method == "Heun":
            k2 = f(x_n + h, y_n + h * k1)
            y_next = y_n + (h/2.0) * (k1 + k2)
        elif method == "Ralston":
            k2 = f(x_n + (2.0/3.0)*h, y_n + (2.0/3.0)*h * k1)
            y_next = y_n + (h/4.0) * (k1 + 3 * k2)
            
        x_vals.append(x_n + h)
        y_vals.append(y_next)
    return x_vals, y_vals

def main():
    x0, y0, x_end = 2.0, 3.0, 2.6
    methods = ["Midpoint", "Heun", "Ralston"]
    step_sizes = [0.03, 0.02, 0.01]
    
    plt.figure(figsize=(15, 5))
    
    for idx, h in enumerate(step_sizes):
        print(f"\n=== RESULTS FOR h = {h} ===")
        print(f"{'x':<5} | {'Exact(RK4)':<12} | {'Heun y':<12} | {'Heun Err':<10} | {'Midpoint Err':<12} | {'Ralston Err'}")
        print("-" * 80)
        
        results = {m: rk2_solve(x0, y0, h, x_end, m) for m in methods}
        x_vals = results["Heun"][0]
        
        errors = {m: [] for m in methods}
        for i, x in enumerate(x_vals):
            exact = exact_rk4_baseline(x)
            err_heun = abs(exact - results["Heun"][1][i])
            err_mid = abs(exact - results["Midpoint"][1][i])
            err_ral = abs(exact - results["Ralston"][1][i])
            
            errors["Heun"].append(err_heun)
            errors["Midpoint"].append(err_mid)
            errors["Ralston"].append(err_ral)
            
            print(f"{x:<5.2f} | {exact:<12.6f} | {results['Heun'][1][i]:<12.6f} | {err_heun:<10.2e} | {err_mid:<12.2e} | {err_ral:<10.2e}")

        # Plot errors for current step size
        plt.subplot(1, 3, idx + 1)
        for m in methods:
            plt.plot(x_vals, errors[m], label=f'{m} Err')
        plt.title(f"Errors (h={h})")
        plt.xlabel("x")
        plt.ylabel("Error")
        plt.legend()
        plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()