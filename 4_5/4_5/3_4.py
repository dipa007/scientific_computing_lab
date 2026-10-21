# question_3_and_4.py
# Newton's Interpolations (Divided, Forward, and Backward) with Error Comparison

import math

def divided_differences(x, y):
    n = len(x)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    return table

def newton_divided_difference(x_data, y_data, x_val):
    table = divided_differences(x_data, y_data)
    n = len(x_data)
    result = table[0][0]
    x_term = 1.0
    for i in range(1, n):
        x_term *= (x_val - x_data[i - 1])
        result += table[0][i] * x_term
    return result

def forward_difference_table(y):
    n = len(y)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    return table

def newton_forward(x_data, y_data, x_val):
    table = forward_difference_table(y_data)
    h = x_data[1] - x_data[0]
    p = (x_val - x_data[0]) / h
    
    result = table[0][0]
    p_term = 1.0
    fact = 1
    
    for i in range(1, len(x_data)):
        p_term *= (p - (i - 1))
        fact *= i
        result += (p_term * table[0][i]) / fact
    return result

def backward_difference_table(y):
    n = len(y)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            table[i][j] = table[i][j - 1] - table[i - 1][j - 1]
    return table

def newton_backward(x_data, y_data, x_val):
    table = backward_difference_table(y_data)
    n = len(x_data)
    h = x_data[1] - x_data[0]
    p = (x_val - x_data[-1]) / h
    
    result = table[n - 1][0]
    p_term = 1.0
    fact = 1
    
    for i in range(1, n):
        p_term *= (p + (i - 1))
        fact *= i
        result += (p_term * table[n - 1][i]) / fact
    return result

def main():
    x_data = [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3]
    y_data = [5.474, 6.050, 6.686, 7.389, 8.166, 9.025, 9.974]
    
    targets = [1.85, 2.25]
    
    # Print table header
    print(f"{'Target x':<10} | {'True Value (e^x)':<18} | {'Method':<25} | {'Interpolated y':<18} | {'Absolute Error'}")
    print("-" * 95)
    
    for x in targets:
        exact = math.exp(x)
        
        # Calculate values using all three methods
        y_div = newton_divided_difference(x_data, y_data, x)
        y_fwd = newton_forward(x_data, y_data, x)
        y_bwd = newton_backward(x_data, y_data, x)
        
        # Calculate absolute errors
        err_div = abs(exact - y_div)
        err_fwd = abs(exact - y_fwd)
        err_bwd = abs(exact - y_bwd)
        
        # Print results formatted to match the requested structure
        print(f"{x:<10} | {exact:<18.8f} | {'Q3: Divided Difference':<25} | {y_div:<18.8f} | {err_div:<.2e}")
        print(f"{'':<10} | {'':<18} | {'Q4: Forward Difference':<25} | {y_fwd:<18.8f} | {err_fwd:<.2e}")
        print(f"{'':<10} | {'':<18} | {'Q4: Backward Difference':<25} | {y_bwd:<18.8f} | {err_bwd:<.2e}")
        print("-" * 95)

if __name__ == "__main__":
    main()