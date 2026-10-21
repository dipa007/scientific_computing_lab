# question_4.py
# Gauss-Legendre 2-point and 3-point formulas

import math

def f1(x):
    return 1.0 / (1.0 + x**2)

def f2(x):
    return math.sqrt(1 - x**2) - x

def gauss_legendre_2pt(func, a, b):
    # Roots and weights for 2-point
    t = [-1.0/math.sqrt(3), 1.0/math.sqrt(3)]
    w = [1.0, 1.0]
    
    mid = (b + a) / 2.0
    half_diff = (b - a) / 2.0
    
    res = 0.0
    for i in range(2):
        x = half_diff * t[i] + mid
        res += w[i] * func(x)
        
    return half_diff * res

def gauss_legendre_3pt(func, a, b):
    # Roots and weights for 3-point
    t = [-math.sqrt(3.0/5.0), 0.0, math.sqrt(3.0/5.0)]
    w = [5.0/9.0, 8.0/9.0, 5.0/9.0]
    
    mid = (b + a) / 2.0
    half_diff = (b - a) / 2.0
    
    res = 0.0
    for i in range(3):
        x = half_diff * t[i] + mid
        res += w[i] * func(x)
        
    return half_diff * res

def trapezoidal_1_interval(func, a, b):
    # 2 evaluations, equivalent to 2-point Gauss
    return ((b - a) / 2.0) * (func(a) + func(b))

def simpson_2_intervals(func, a, b):
    # 3 evaluations, equivalent to 3-point Gauss
    h = (b - a) / 2.0
    return (h / 3.0) * (func(a) + 4*func(a+h) + func(b))

def main():
    integrals = [
        ("Integral Q2", f1, 0.0, 1.0, math.pi / 4.0),
        ("Integral Q3", f2, 0.0, 1.0/math.sqrt(2), math.pi / 8.0)
    ]
    
    print("GAUSS-LEGENDRE VS NEWTON-COTES (EQUAL FUNCTION EVALUATIONS)")
    for name, func, a, b, true_val in integrals:
        print(f"\n{'='*80}\n{name}: True Value = {true_val:.9f}")
        print("-" * 80)
        print(f"{'Method':<20} | {'Evaluations':<15} | {'Result':<15} | {'Error':<15}")
        print("-" * 80)
        
        # 2 Evaluations comparison
        trap_res = trapezoidal_1_interval(func, a, b)
        gl2_res = gauss_legendre_2pt(func, a, b)
        
        print(f"{'Trapezoidal (N=1)':<20} | {'2':<15} | {trap_res:<15.9f} | {abs(true_val - trap_res):<15.2e}")
        print(f"{'Gauss-Legendre 2pt':<20} | {'2':<15} | {gl2_res:<15.9f} | {abs(true_val - gl2_res):<15.2e}")
        print("-" * 80)
        
        # 3 Evaluations comparison
        simp_res = simpson_2_intervals(func, a, b)
        gl3_res = gauss_legendre_3pt(func, a, b)
        
        print(f"{'Simpson 1/3 (N=2)':<20} | {'3':<15} | {simp_res:<15.9f} | {abs(true_val - simp_res):<15.2e}")
        print(f"{'Gauss-Legendre 3pt':<20} | {'3':<15} | {gl3_res:<15.9f} | {abs(true_val - gl3_res):<15.2e}")

if __name__ == "__main__":
    main()