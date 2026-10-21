# question_5.py
# Comparing FE, BE, and Mod Euler for Q3 and Q4

import math

def true_sol_q3(t):
    return 2 * math.exp(t) + t**2 - t - 1

def exact_rk4_q4(x_target):
    x, y, h = 2.0, 3.0, 1e-5
    def f(x, y): return x * (y - x)
    while x < x_target - h/2:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x += h
    return y

def solve_q3(h):
    t_vals, y_fe, y_be, y_me = [0.0], [1.0], [1.0], [1.0]
    while t_vals[-1] < 1.0 - 1e-9:
        t_n = t_vals[-1]
        t_next = t_n + h
        
        # Forward Euler
        y_fe.append(y_fe[-1] + h * (y_fe[-1] + 3*t_n - t_n**2))
        
        # Backward Euler (Implicit solved: y = y + h(y + 3t - t^2))
        y_be.append((y_be[-1] + h * (3*t_next - t_next**2)) / (1.0 - h))
        
        # Modified Euler
        def f(t, y): return y + 3*t - t**2
        y_predict = y_me[-1] + h * f(t_n, y_me[-1])
        y_me.append(y_me[-1] + (h/2.0) * (f(t_n, y_me[-1]) + f(t_next, y_predict)))
        
        t_vals.append(t_next)
    return t_vals, y_fe, y_be, y_me

def solve_q4(h):
    x_vals, y_fe, y_be, y_me = [2.0], [3.0], [3.0], [3.0]
    while x_vals[-1] < 2.6 - 1e-9:
        x_n = x_vals[-1]
        x_next = x_n + h
        
        # Forward Euler
        y_fe.append(y_fe[-1] + h * (x_n * (y_fe[-1] - x_n)))
        
        # Backward Euler (Implicit solved: y = y + h(x(y - x)))
        y_be.append((y_be[-1] - h * x_next**2) / (1.0 - h * x_next))
        
        # Modified Euler
        def f(x, y): return x * (y - x)
        y_predict = y_me[-1] + h * f(x_n, y_me[-1])
        y_me.append(y_me[-1] + (h/2.0) * (f(x_n, y_me[-1]) + f(x_next, y_predict)))
        
        x_vals.append(x_next)
    return x_vals, y_fe, y_be, y_me

def print_table(title, ind_vals, y_fe, y_be, y_me, exact_func):
    print(f"\n{title}")
    print("-" * 90)
    print(f"{'Ind Var':<8} | {'Exact':<12} | {'F.E. Err':<15} | {'B.E. Err':<15} | {'Mod Euler Err':<15}")
    print("-" * 90)
    for i, var in enumerate(ind_vals):
        exact = exact_func(var)
        err_fe = abs(exact - y_fe[i])
        err_be = abs(exact - y_be[i])
        err_me = abs(exact - y_me[i])
        print(f"{var:<8.2f} | {exact:<12.6f} | {err_fe:<15.2e} | {err_be:<15.2e} | {err_me:<15.2e}")

def main():
    print("=== QUESTION 3 PROBLEM ===")
    for h in [0.1, 0.05]:
        t_vals, y_fe, y_be, y_me = solve_q3(h)
        print_table(f"Q3 Data (h={h})", t_vals, y_fe, y_be, y_me, true_sol_q3)
        
    print("\n=== QUESTION 4 PROBLEM ===")
    for h in [0.03, 0.01]:
        x_vals, y_fe, y_be, y_me = solve_q4(h)
        print_table(f"Q4 Data (h={h})", x_vals, y_fe, y_be, y_me, exact_rk4_q4)

if __name__ == "__main__":
    main()