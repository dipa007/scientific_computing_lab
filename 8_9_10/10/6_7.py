# question_6_7.py
# RK4 for y' = xy + y^2 and Order of Convergence Calculation

import matplotlib.pyplot as plt
import math

def f(x, y):
    return x * y + y**2

def exact_rk4_baseline(x_target):
    x, y, h = 0.0, 1.0, 1e-6 # Ultra-fine for true comparison
    while x < x_target - h/2:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x += h
    return y

def rk4_solve(x0, y0, h, x_end):
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_n, y_n = x_vals[-1], y_vals[-1]
        
        k1 = h * f(x_n, y_n)
        k2 = h * f(x_n + h/2.0, y_n + k1/2.0)
        k3 = h * f(x_n + h/2.0, y_n + k2/2.0)
        k4 = h * f(x_n + h, y_n + k3)
        
        y_next = y_n + (k1 + 2*k2 + 2*k3 + k4) / 6.0
        
        x_vals.append(x_n + h)
        y_vals.append(y_next)
    return x_vals, y_vals

def main():
    x0, y0, x_end = 0.0, 1.0, 0.5
    step_sizes = [0.05, 0.025]
    final_errors = {}
    
    plt.figure(figsize=(12, 5))
    
    print("=== QUESTION 6: RK4 COMPUTATIONS ===")
    for h in step_sizes:
        x_vals, y_vals = rk4_solve(x0, y0, h, x_end)
        
        print(f"\nStep length h = {h}")
        print(f"{'x':<5} | {'Exact':<15} | {'RK4 y':<15} | {'Absolute Error'}")
        print("-" * 65)
        
        err_list = []
        for i, x in enumerate(x_vals):
            exact = exact_rk4_baseline(x)
            err = abs(exact - y_vals[i])
            err_list.append(err)
            print(f"{x:<5.3f} | {exact:<15.9f} | {y_vals[i]:<15.9f} | {err:<15.2e}")
            
        final_errors[h] = err_list[-1]
        
        # Plotting
        plt.subplot(1, 2, 1)
        plt.plot(x_vals, y_vals, label=f'RK4 (h={h})')
        plt.subplot(1, 2, 2)
        plt.plot(x_vals, err_list, label=f'Error (h={h})')

    plt.subplot(1, 2, 1)
    plt.title("Numerical Solutions")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.title("Absolute Errors")
    plt.xlabel('x')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    
    # QUESTION 7
    print("\n\n=== QUESTION 7: COMPUTATIONAL ORDER OF CONVERGENCE ===")
    e_h = final_errors[0.05]
    e_half_h = final_errors[0.025]
    
    # Order of convergence p ≈ log2(E_h / E_h/2)
    order_p = math.log2(e_h / e_half_h)
    
    print("-" * 60)
    print(f"{'h1':<10} | {'Error 1 (E_h)':<18} | {'h2':<10} | {'Error 2 (E_h/2)':<18} | {'Order (p)'}")
    print("-" * 60)
    print(f"{0.05:<10} | {e_h:<18.2e} | {0.025:<10} | {e_half_h:<18.2e} | {order_p:.4f}")
    print("-" * 60)
    print("Remarks:")
    print("The computationally derived order of convergence is approximately 4, confirming that the standard Runge-Kutta method is an O(h^4) scheme.")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()