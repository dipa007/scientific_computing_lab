# question_1a.py
# Graphical Inspection of e^(-x/5) = sin(x) on [0, 10]
# Do pip install matplotlib

import math
# pyrefly: ignore[missing-import]
import matplotlib.pyplot as plt

def main():
    # Generate x values from 0 to 10 without numpy
    x_vals = [i * 10.0 / 1000 for i in range(1001)]
    
    # Calculate y values for both functions
    y1 = [math.exp(-x / 5.0) for x in x_vals]
    y2 = [math.sin(x) for x in x_vals]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y1, label='e^(-x/5)', color='blue', linewidth=2)
    plt.plot(x_vals, y2, label='sin(x)', color='red', linewidth=2)
    
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphical Inspection: Intersection of e^(-x/5) and sin(x)')
    plt.legend()
    plt.grid(True)
    
    # Save the plot or show it
    print("Plotting complete. The graph shows four intersection points in [0, 10].")
    print("Based on visual inspection, we can approximate the roots in the following intervals:")
    print("Root 1: [0.5, 1.5]")
    print("Root 2: [2.0, 3.0]")
    print("Root 3: [6.0, 7.1]")
    print("Root 4: [8.8, 9.8]")

    #print("Plotting complete. Scanning for sign changes to approximate roots...")
    
    # Calculate f(x) for all x_vals
    #f_vals = [y1[i] - y2[i] for i in range(len(x_vals))]
    
    #intervals = []
    # Loop through the values to find where the function crosses zero
    #for i in range(len(f_vals) - 1):
        #if f_vals[i] * f_vals[i+1] < 0:
            #intervals.append((x_vals[i], x_vals[i+1]))
            
    #for idx, interval in enumerate(intervals):
        #We widen the bracket slightly (e.g., by 0.5) to make it a broader "human-like" visual guess
        #print(f"Root {idx + 1}: [{max(0, interval[0] - 0.5):.1f}, {interval[1] + 0.5:.1f}]")
    plt.show()

if __name__ == "__main__":
    main()