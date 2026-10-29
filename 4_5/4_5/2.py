def divided_differences(x, y):
    n = len(x)
    table = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])
    return table

def evaluate_newton_poly(table, x_data, x_val):
    n = len(x_data)
    result = table[0][0]
    x_term = 1.0
    for i in range(1, n):
        x_term *= (x_val - x_data[i - 1])
        result += table[0][i] * x_term
    return result

def main():
    t_data = [10, 15, 20, 22.5]
    v_data = [227.04, 362.78, 517.35, 602.97]
    t_target = 16
    n = len(t_data)
    diff_table = divided_differences(t_data, v_data)
    v_target = evaluate_newton_poly(diff_table, t_data, t_target)
    
    print("Divided Difference Table (Selected Points):")
    print(f"{'t':<8} | {'v(t)':<10} | {'1st Diff':<10} | {'2nd Diff':<10} | {'3rd Diff'}")
    print("-" * 60)
    
    for i in range(n):
        row_str = f"{t_data[i]:<8} | {diff_table[i][0]:<10.4f}"
        for j in range(1, n):
            if i < n - j:
                row_str += f" | {diff_table[i][j]:<10.4f}"
            else:
                row_str += f" | {'':<10}"
        print(row_str)
    print(f"\nVelocity at t = {t_target} seconds (3rd order interpolation) is: {v_target:.4f}")

if __name__ == "__main__":
    main()