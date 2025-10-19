# Simulation Script

This Python script, `simulation2.py`, runs a simulation to generate data based on a linear equation with added noise. It then performs a linear regression on the generated data to find the best-fit line.

## Functionality

The script performs the following steps:

1.  **Data Generation**: It generates a dataset of `(weight, height)` pairs. The `weight` values are randomly generated, and the corresponding `height` values are calculated using the equation `height = a * weight + b + r`, where `a` and `b` are predefined coefficients and `r` is a random noise factor.

2.  **Linear Regression**: It calculates the line of best fit for the generated data using `numpy.polyfit`.

3.  **Plotting**: It creates a scatter plot of the data points and overlays the calculated regression line. The plot includes a title, axis labels, a legend, and a text box displaying the data generation and linear regression equations.

4.  **Output**: The script saves the generated plot as an image file at `Documentation/simulation_results.png` and the equations to a text file at `Documentation/simulation_equations.txt`.

## How to Run

To run the simulation, execute the script from your terminal:

```bash
python simulation2.py
```
