# question_2.py
# Euler and Modified Euler for y' = xy + y^2

def f(x, y):
    return x * y + y**2

def exact_rk4_baseline(x_target):
    # Generates highly accurate baseline since analytical is complex
    x, y = 0.0, 1.0
    h = 1e-5
    while x < x_target - h/2:
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6.0
        x += h
    return y

def euler(x0, y0, h, x_end):
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_n, y_n = x_vals[-1], y_vals[-1]
        y_vals.append(y_n + h * f(x_n, y_n))
        x_vals.append(x_n + h)
    return x_vals, y_vals

def modified_euler(x0, y0, h, x_end):
    x_vals, y_vals = [x0], [y0]
    while x_vals[-1] < x_end - 1e-9:
        x_n, y_n = x_vals[-1], y_vals[-1]
        y_predict = y_n + h * f(x_n, y_n)
        y_correct = y_n + (h / 2.0) * (f(x_n, y_n) + f(x_n + h, y_predict))
        y_vals.append(y_correct)
        x_vals.append(x_n + h)
    return x_vals, y_vals

def main():
    x0, y0 = 0.0, 1.0
    h = 0.1
    x_end = 0.5
    
    x_eu, y_eu = euler(x0, y0, h, x_end)
    x_me, y_me = modified_euler(x0, y0, h, x_end)
    
    print("Q2: y' = xy + y^2, y(0)=1 (h=0.1)")
    print("-" * 80)
    print(f"{'x':<5} | {'Exact(RK4)':<15} | {'Euler y':<15} | {'Euler Err':<12} | {'Mod Euler y':<15} | {'Mod Err':<12}")
    print("-" * 80)
    
    for i in range(len(x_eu)):
        x_val = x_eu[i]
        true_y = exact_rk4_baseline(x_val)
        
        err_eu = abs(true_y - y_eu[i])
        err_me = abs(true_y - y_me[i])
        
        print(f"{x_val:<5.2f} | {true_y:<15.6f} | {y_eu[i]:<15.6f} | {err_eu:<12.2e} | {y_me[i]:<15.6f} | {err_me:<12.2e}")

if __name__ == "__main__":
    main()