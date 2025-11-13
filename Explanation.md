# Theoretical Explanation: Weight vs Height Simulation and Regression Analysis

## Overview
This project simulates the relationship between human height and weight using statistical methods and linear regression. The simulation generates random samples from normal distributions and then finds the best-fit line through the data.

## Part 1: Data Generation Model

### Normal Distribution
Both height and weight are generated using **normal (Gaussian) distributions**, which are commonly used to model natural phenomena like human measurements.

#### Height Distribution
- **Mean (μ):** 170 cm
- **Standard Deviation (σ):** 10 cm
- **Variance (σ²):** 100 cm²
- **Mathematical Form:** $H \sim N(170, 100)$

This means most people's heights cluster around 170 cm, with about 68% of the population falling between 160-180 cm (within one standard deviation).

#### Weight Distribution
- **Mean (μ):** 75 kg
- **Standard Deviation (σ):** 15 kg
- **Variance (σ²):** 225 kg²
- **Mathematical Form:** $W \sim N(75, 225)$

Similarly, most weights cluster around 75 kg, with about 68% of the population between 60-90 kg.

### Why Normal Distribution?
Natural human measurements follow approximately normal distributions due to the **Central Limit Theorem**: many independent genetic and environmental factors combine to create measurements that are approximately normally distributed.

---

## Part 2: Linear Regression Analysis

### What is Linear Regression?
Linear regression finds the best-fit straight line through a set of data points. The goal is to model the relationship between an independent variable (x) and a dependent variable (y).

**In this project:**
- **Independent variable (x):** Height (cm)
- **Dependent variable (y):** Weight (kg)

### The Linear Model
The regression line follows the equation:

$$\hat{y} = mx + c$$

Where:
- $\hat{y}$ is the predicted weight
- $x$ is the height
- $m$ is the **slope** (how much weight changes per cm of height)
- $c$ is the **y-intercept** (predicted weight when height is 0)

### Least Squares Method
The regression line is calculated using the **Least Squares Method**, which minimizes the sum of squared vertical distances between the data points and the line.

**Objective:** Minimize $\sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

Where:
- $y_i$ are the actual observed values
- $\hat{y}_i$ are the predicted values from the regression line

### Formulas for Slope and Intercept

$$m = \frac{n\sum xy - \sum x \sum y}{n\sum x^2 - (\sum x)^2}$$

$$c = \bar{y} - m\bar{x}$$

Where:
- $n$ is the number of data points
- $\bar{x}$ and $\bar{y}$ are the means of x and y respectively

---

## Part 3: Simulation 2 - Random Error Model

### Extended Model with Random Noise
The second simulation (simulation2.py) uses a more realistic model:

$$y = ax + b + r$$

Where:
- $y$ is the predicted height
- $x$ is the weight
- $a$ is the slope
- $b$ is the intercept
- $r$ is a random error term (noise)

### Why Add Random Noise?
Real-world data is never perfectly linear. Random noise ($r$) represents:
- Measurement errors
- Genetic variations not explained by height alone
- Environmental factors
- Other unmodeled variables

This creates a more realistic simulation that better reflects actual data patterns.

---
![Simulation Graph](Documentation/simulation_results.png)

## Key Concepts

### Correlation
The relationship between height and weight shows **positive correlation**: taller people tend to weigh more. However, the relationship is not perfect—there's considerable variation.

### Coefficient of Determination (R²)
Though not explicitly calculated in this project, R² measures how well the regression line fits the data (0 ≤ R² ≤ 1). Values closer to 1 indicate a better fit.

### Residuals
The differences between actual data points and the regression line are called **residuals**. In a good model, residuals should be:
- Small in magnitude
- Randomly distributed (no pattern)
- Approximately normally distributed

---

## Statistical Interpretation

### What the Results Tell Us
1. **The slope (m):** Indicates how many kg of weight increase per cm of height increase
2. **The intercept (c):** Theoretical weight when height is zero (usually not meaningful in practice)
3. **The scatter:** Shows the variability and uncertainty in the relationship

### Practical Application
In real-world scenarios, this regression model could be used to:
- Estimate typical weight for a given height
- Identify individuals who deviate significantly from the average relationship
- Understand population health metrics
- Build predictive models for body mass calculations

---

## Visualization Interpretation

The scatter plot shows:
- **Blue dots:** Actual data samples
- **Red line:** Best-fit regression line showing the average trend
- **Spread around the line:** Represents the natural variation in the relationship

The wider the spread, the more variability exists in the relationship between height and weight that isn't explained by height alone.

---

## References
- Normal Distribution: https://en.wikipedia.org/wiki/Normal_distribution
- Linear Regression: https://en.wikipedia.org/wiki/Linear_regression
- Least Squares Method: https://en.wikipedia.org/wiki/Least_squares
