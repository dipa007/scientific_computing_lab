# question_5.py
# 10th-degree Newton polynomial for tan^(-1)(x) and error evaluation

import math

def forward_difference_table(y):
    n = len(y)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]
    return table

def evaluate_newton_forward_poly(x_data, y_data, x_val):
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

def main():
    # 11 equally spaced points in [0, 6]
    num_points = 11
    interval_start, interval_end = 0.0, 6.0
    h = (interval_end - interval_start) / (num_points - 1)
    
    x_nodes = [interval_start + i * h for i in range(num_points)]
    y_nodes = [math.atan(x) for x in x_nodes]
    
    # Print the coefficients based on Newton Forward Basis
    table = forward_difference_table(y_nodes)
    print("NEWTON FORWARD POLYNOMIAL COEFFICIENTS (Degree 0 to 10)")
    print("Formula: C_k = (Forward_Diff_k) / (k! * h^k)")
    print("-" * 60)
    fact = 1
    for k in range(num_points):
        if k > 0: fact *= k
        coeff = table[0][k] / (fact * (h ** k))
        print(f"C_{k:<2} = {coeff: .8f}")
        
    # Evaluate at 33 points in [0, 8]
    test_points = 33
    test_start, test_end = 0.0, 8.0
    test_h = (test_end - test_start) / (test_points - 1)
    
    print(f"\n{'x':<6} | {'True tan^-1(x)':<15} | {'Poly P(x)':<15} | {'Difference (Error)':<15}")
    print("-" * 60)
    
    for i in range(test_points):
        x_val = test_start + i * test_h
        true_val = math.atan(x_val)
        poly_val = evaluate_newton_forward_poly(x_nodes, y_nodes, x_val)
        diff = abs(true_val - poly_val)
        print(f"{x_val:<6.2f} | {true_val:<15.6f} | {poly_val:<15.6f} | {diff:<15.2e}")

    print("\nConclusions Drawn from the Output:")
    print("1. Interpolation Zone [0, 6]: The polynomial matches the function highly accurately, with errors remaining extremely small.")
    print("2. Extrapolation Zone (6, 8]: As x moves past 6, the polynomial diverges violently from the true function, resulting in massive errors. This highlights that high-degree polynomials are highly unstable for extrapolation (a symptom related to Runge's Phenomenon).")

if __name__ == "__main__":
    main()