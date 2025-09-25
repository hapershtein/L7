import numpy as np
import matplotlib.pyplot as plt

def generate_person_data(num_samples=1000):
    """
    Generates random samples of height and weight.
    Assumes a normal distribution for both.
    """
    # Height in cm: mean=170, std=10
    heights = np.random.normal(170, 10, num_samples)
    # Weight in kg: mean=75, std=15
    weights = np.random.normal(75, 15, num_samples)
    return heights, weights

def run_simulation():
    """
    Runs the simulation, generates data, and plots it.
    """
    heights, weights = generate_person_data()

    # Calculate regression line
    m, c = np.polyfit(heights, weights, 1)
    
    # Sort values for plotting the regression line smoothly
    sorted_indices = np.argsort(heights)
    sorted_heights = heights[sorted_indices]
    regression_line = m * sorted_heights + c

    # Print the equations
    print("Data generation model (Normal Distribution):")
    print("Height ~ N(μ=170, σ²=100)")
    print("Weight ~ N(μ=75, σ²=225)")
    print("\n" + "="*30 + "\n")
    print("Linear Regression Line Equation:")
    print(f"Weight = {m:.2f} * Height + {c:.2f}")
    print("\n" + "="*30 + "\n")

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.scatter(heights, weights, alpha=0.5, label='Data Samples')
    plt.plot(sorted_heights, regression_line, color='red', linewidth=2, label=f'Regression Line: y={m:.2f}x+{c:.2f}')
    plt.title('Simulation of Human Height and Weight')
    plt.xlabel('Height (cm)')
    plt.ylabel('Weight (kg)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    run_simulation()
