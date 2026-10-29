def add_poly(p1, p2):
    max_len = max(len(p1), len(p2))
    result = [0.0] * max_len
    for i in range(len(p1)):
        result[i] += p1[i]
    for i in range(len(p2)):
        result[i] += p2[i]
    return result

def mul_poly(p1, p2):
    result = [0.0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j] += p1[i] * p2[j]
    return result

def format_poly(poly):
    terms = []
    for i in range(len(poly)-1, -1, -1):
        coef = poly[i]
        if abs(coef) < 1e-9:
            continue
        
        if terms:
            sign = " + " if coef >= 0 else " - "
        else:
            sign = "-" if coef < 0 else ""
            
        val = abs(coef)
        
        if i == 0:
            term = f"{val:.4f}"
        elif i == 1:
            term = f"{val:.4f}x"
        else:
            term = f"{val:.4f}x^{i}"
        terms.append(sign + term)
    return "".join(terms) if terms else "0"

def lagrange_interpolation(x_data, y_data, x_val):
    n = len(x_data)
    total_poly = []
    result = 0.0
    for i in range(n):
        term_val = y_data[i]
        term_poly = [y_data[i]] 
        for j in range(n):
            if i != j:
                denominator = x_data[i] - x_data[j]
                term_val = term_val * (x_val - x_data[j]) / denominator
                multiplier_poly = [-x_data[j] / denominator, 1.0 / denominator]
                term_poly = mul_poly(term_poly, multiplier_poly)    
        result += term_val
        total_poly = add_poly(total_poly, term_poly)
    polynomial_str = format_poly(total_poly)
    return result, polynomial_str

def main():
    x_data = [5, 7, 11, 13, 17]
    y_data = [150, 392, 1452, 2366, 5202]
    x_target = 10
    y_target, polynomial = lagrange_interpolation(x_data, y_data, x_target)
    print("LAGRANGE INTERPOLATION")
    print("-" * 60)
    print(f"Value of y at x = {x_target} is: {y_target}")
    print("\nLagrange Interpolating Polynomial P(x):")
    print(polynomial)

if __name__ == "__main__":
    main()