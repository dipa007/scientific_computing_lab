# question_5.py
# Jacobi Method for Linear Systems with fixed iterations and tolerance

def jacobi_iteration(A, B, x_old):
    n = len(A)
    x_new = [0.0] * n
    for i in range(n):
        sum_ax = 0.0
        for j in range(n):
            if i != j:
                sum_ax += A[i][j] * x_old[j]
        x_new[i] = (B[i] - sum_ax) / A[i][i]
    return x_new

def calc_error(x_new, x_old):
    # Max absolute difference between iterations
    return max(abs(x_new[i] - x_old[i]) for i in range(len(x_new)))

def main():
    # REORDERED strictly diagonally dominant matrix
    A = [
        [4.0, 1.0, -1.0, 1.0],  # old eq 2
        [1.0, 4.0, -1.0, -1.0], # old eq 1
        [-1.0, -1.0, 5.0, 1.0], # old eq 4
        [1.0, -1.0, 1.0, 3.0]   # old eq 3
    ]
    B = [-2.0, -1.0, 0.0, 1.0]
    
    x = [0.0, 0.0, 0.0, 0.0] # Initial guess
    tol = 1e-3
    
    print("JACOBI METHOD ERROR OBSERVATION (Table Format)")
    print("-" * 65)
    print(f"{'Iteration Phase':<20} | {'Vector x [x1, x2, x3, x4]':<25} | {'Step Error'}")
    print("-" * 65)
    
    # Run fixed iterations to observe effect
    for k in range(1, 21):
        x_next = jacobi_iteration(A, B, x)
        error = calc_error(x_next, x)
        x = x_next
        
        if k == 10:
            formatted_x = "[" + ", ".join([f"{val:.3f}" for val in x]) + "]"
            print(f"{'After 10 Iters':<20} | {formatted_x:<25} | {error:.6f}")
        if k == 20:
            formatted_x = "[" + ", ".join([f"{val:.3f}" for val in x]) + "]"
            print(f"{'After 20 Iters (2x)':<20} | {formatted_x:<25} | {error:.6f}")
            
    print("\nConclusion: Doubling the iterations significantly reduces the error.")
    
    # Run until tolerance is met
    x_tol = [0.0, 0.0, 0.0, 0.0]
    iters = 0
    while True:
        x_next = jacobi_iteration(A, B, x_tol)
        error = calc_error(x_next, x_tol)
        x_tol = x_next
        iters += 1
        if error < tol:
            break
            
    print(f"\nJacobi method reached TOL = 10^-3 at iteration: {iters}")

if __name__ == "__main__":
    main()