import math
import matplotlib.pyplot as plt

def main():
    x_vals = [i * 10.0 / 1000 for i in range(1001)]
    y1 = [math.exp(-x / 5.0) for x in x_vals]
    y2 = [math.sin(x) for x in x_vals]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y1, label='e^(-x/5)', color='blue', linewidth=2)
    plt.plot(x_vals, y2, label='sin(x)', color='red', linewidth=2)
    
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graphical Inspection: Intersection of e^(-x/5) and sin(x)')
    plt.legend()
    plt.grid(True)
    
    print("Plotting complete. The graph shows four intersection points in [0, 10].")
    print("Based on visual inspection, we can approximate the roots in the following intervals:")
    print("Root 1: [0.5, 1.5]")
    print("Root 2: [2.0, 3.0]")
    print("Root 3: [6.0, 7.1]")
    print("Root 4: [8.8, 9.8]")
    plt.show()

if __name__ == "__main__":
    main()