# question_1.py
# Euler and Backward Euler methods for two initial value problems

#This script solves $\frac{dy}{dx} = f(x,y)$ with two experiments as instructed:   $f(x,y) = x + y, y(0)=1$. (True Solution: $y = 2e^x - x - 1$)   $f(x,y) = -2y, y(0)=1$. (True Solution: $y = e^{-2x}$)

import math
import matplotlib.pyplot as plt

def true_sol_1(x):
    return 2 * math.exp(x) - x - 1

def true_sol_2(x):
    return math.exp(-2 * x)

def forward_euler(f, x0, y0, h, x_end):
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_n = x_vals[-1]
        y_n = y_vals[-1]
        y_next = y_n + h * f(x_n, y_n)
        x_vals.append(x_n + h)
        y_vals.append(y_next)
    return x_vals, y_vals

def backward_euler_1(x0, y0, h, x_end):
    # Algebraic manipulation for y' = x + y -> y_{n+1} = (y_n + h*x_{n+1}) / (1 - h)
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_next = x_vals[-1] + h
        y_next = (y_vals[-1] + h * x_next) / (1.0 - h)
        x_vals.append(x_next)
        y_vals.append(y_next)
    return x_vals, y_vals

def backward_euler_2(x0, y0, h, x_end):
    # Algebraic manipulation for y' = -2y -> y_{n+1} = y_n / (1 + 2h)
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_next = x_vals[-1] + h
        y_next = y_vals[-1] / (1.0 + 2 * h)
        x_vals.append(x_next)
        y_vals.append(y_next)
    return x_vals, y_vals

def run_experiment(exp_name, f, true_f, be_func, x0, y0, x_end):
    print(f"\n{exp_name}")
    print("-" * 80)
    for h in [0.1, 0.05]:
        x_fe, y_fe = forward_euler(f, x0, y0, h, x_end)
        x_be, y_be = be_func(x0, y0, h, x_end)
        
        print(f"\nStep length h = {h}")
        print(f"{'x':<5} | {'True y':<15} | {'FE Error':<15} | {'BE Error':<15}")
        print("-" * 60)
        
        err_fe_list, err_be_list = [], []
        for i in range(len(x_fe)):
            t_y = true_f(x_fe[i])
            err_fe = abs(t_y - y_fe[i])
            err_be = abs(t_y - y_be[i])
            err_fe_list.append(err_fe)
            err_be_list.append(err_be)
            print(f"{x_fe[i]:<5.2f} | {t_y:<15.6f} | {err_fe:<15.2e} | {err_be:<15.2e}")
            
        plt.plot(x_fe, err_fe_list, label=f'FE Error (h={h})')
        plt.plot(x_be, err_be_list, label=f'BE Error (h={h})', linestyle='--')

def main():
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    run_experiment("Experiment 1: y' = x + y", lambda x, y: x + y, true_sol_1, backward_euler_1, 0.0, 1.0, 1.0)
    plt.title("Errors for y' = x + y")
    plt.xlabel('x')
    plt.ylabel('Absolute Error')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    run_experiment("Experiment 2: y' = -2y", lambda x, y: -2 * y, true_sol_2, backward_euler_2, 0.0, 1.0, 1.0)
    plt.title("Errors for y' = -2y")
    plt.xlabel('x')
    plt.ylabel('Absolute Error')
    plt.legend()
    plt.grid(True)
    
    print("\nRemarks:")
    print("1. Decreasing the step size from h=0.1 to h=0.05 reduces the error for both methods by approximately a factor of 2, confirming they are first-order methods.")
    print("2. Backward Euler (Implicit) often provides better numerical stability, though in Experiment 1 it overestimates while Forward Euler underestimates.")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()