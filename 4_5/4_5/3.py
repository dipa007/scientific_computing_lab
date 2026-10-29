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

def main():
    x_data = [1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3]
    y_data = [5.474, 6.050, 6.686, 7.389, 8.166, 9.025, 9.974]
    targets = [1.85, 2.25]
    print("Newton's Interpolation")
    print("-" * 40)
    for x in targets:
        y_interp = newton_divided_difference(x_data, y_data, x)
        print(f"Value of y at x = {x} is: {y_interp:.8f}")
        
if __name__ == "__main__":
    main()