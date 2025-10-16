import numpy as np
import matplotlib.pyplot as plt

def run_simulation():
    """
    Runs a simulation based on y = ax + b + r, plots it, and shows equations.
    """
    num_samples = 1000
    
    # Define the parameters for the data generation equation
    a = 2.0
    b = 25.0
    
    # Generate x (weight) values
    weights = 50 + 50 * np.random.rand(num_samples)
    
    # Generate random noise (r)
    random_noise = np.random.normal(0, 15, num_samples)
    
    # Calculate y (height) using the equation y = ax + b + r
    heights = a * weights + b + random_noise
    
    # Calculate the regression line
    m, c = np.polyfit(weights, heights, 1)
    
    # Sort values for plotting the regression line smoothly
    sorted_indices = np.argsort(weights)
    sorted_weights = weights[sorted_indices]
    regression_line = m * sorted_weights + c

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(weights, heights, alpha=0.5, label='Data Samples')
    ax.plot(sorted_weights, regression_line, color='red', linewidth=2, label='Regression Line')

    ax.set_title('Simulation based on y = ax + b + r')
    ax.set_xlabel('Weight (kg)')
    ax.set_ylabel('Height (cm)')
    ax.legend(loc='upper left')
    ax.grid(True)

    # Prepare the text for the text box
    equation_text = (
        f"Data Generation Equation:\n"
        f"Height = {a:.2f} * Weight + {b:.2f} + r\n\n"
        f"Linear Regression Equation:\n"
        f"Height = {m:.2f} * Weight + {c:.2f}"
    )

    # Add the text box to the plot
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, equation_text, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)

    # Save the plot to a file
    output_path = 'Documentation/simulation_results.png'
    plt.savefig(output_path)
    print(f"Plot saved to {output_path}")

    # Save the equations to a text file
    equations_path = 'Documentation/simulation_equations.txt'
    with open(equations_path, 'w') as f:
        f.write(equation_text)
    print(f"Equations saved to {equations_path}")

    plt.close()  # Close the plot to free up memory

if __name__ == '__main__':
    run_simulation()
