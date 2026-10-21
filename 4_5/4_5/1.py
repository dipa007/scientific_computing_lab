# question_1.py
# Lagrange interpolation to find y at x = 10

def lagrange_interpolation(x_data, y_data, x_val):
    n = len(x_data)
    result = 0.0
    poly_terms = []
    
    for i in range(n):
        term = y_data[i]
        term_num_str = f"{y_data[i]}"
        term_den_val = 1.0
        
        for j in range(n):
            if i != j:
                term = term * (x_val - x_data[j]) / (x_data[i] - x_data[j])
                term_num_str += f"*(x - {x_data[j]})"
                term_den_val *= (x_data[i] - x_data[j])
                
        result += term
        # Build string representation of the polynomial term
        poly_terms.append(f"[{term_num_str} / {term_den_val}]")
        
    polynomial_str = " + \n".join(poly_terms)
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