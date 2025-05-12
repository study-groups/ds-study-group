import numpy as np
import matplotlib.pyplot as plt

# Given data
microbiome_diversity_index = np.array([
    2.35, 3.10, 1.85, 2.95, 2.40, 3.20, 1.90, 2.70, 2.50, 3.00
])

BMI = np.array([
    22.4, 20.1, 30.2, 25.6, 28.3, 21.7, 29.5, 23.8, 26.1, 22.0
])

# Calculate means
x_bar = np.mean(microbiome_diversity_index)
y_bar = np.mean(BMI)

# Calculate the slope (beta_1)
beta_1 = np.sum((microbiome_diversity_index - x_bar) * (BMI - y_bar)) / np.sum((microbiome_diversity_index - x_bar)**2)

# Calculate the intercept (beta_0)
beta_0 = y_bar - beta_1 * x_bar

# Calculate R^2
y_pred = beta_0 + beta_1 * microbiome_diversity_index
ss_res = np.sum((BMI - y_pred)**2)
ss_tot = np.sum((BMI - y_bar)**2)
r_squared = 1 - (ss_res / ss_tot)

# Print the LMS estimates and R^2
print(f"Intercept (beta_0): {beta_0:.2f}")
print(f"Slope (beta_1): {beta_1:.2f}")
print(f"R^2: {r_squared:.2f}")


from scipy import stats

# Calculate standard errors
n = len(BMI)
y_pred = beta_0 + beta_1 * microbiome_diversity_index
MSE = np.sum((BMI - y_pred)**2) / (n - 2)
SE_beta_1 = np.sqrt(MSE / np.sum((microbiome_diversity_index - x_bar)**2))
SE_beta_0 = SE_beta_1 * np.sqrt((1/n) + (x_bar**2) / np.sum((microbiome_diversity_index - x_bar)**2))

# Calculate t-scores for 95% confidence intervals
t_score = stats.t.ppf(1 - 0.025, df=n - 2)

# Calculate confidence intervals
CI_beta_1 = (beta_1 - t_score * SE_beta_1, beta_1 + t_score * SE_beta_1)
CI_beta_0 = (beta_0 - t_score * SE_beta_0, beta_0 + t_score * SE_beta_0)

# Calculate adjusted R^2
adjusted_R2 = 1 - (1-r_squared) * (n - 1) / (n - 2 - 1)

# Print the confidence intervals and adjusted R^2
print(f"95% CI for slope (beta_1): {CI_beta_1}")
print(f"95% CI for intercept (beta_0): {CI_beta_0}")
print(f"Adjusted R^2: {adjusted_R2:.2f}")



# Scatter plot of the data points
plt.scatter(microbiome_diversity_index, BMI, color='blue', label='Data points')

# Plot the regression line
x_values = np.linspace(min(microbiome_diversity_index), max(microbiome_diversity_index), 100)
y_values = beta_0 + beta_1 * x_values
plt.plot(x_values, y_values, color='red', label=f'Regression Line\n$y = {beta_0:.2f} + {beta_1:.2f}x$\n$R^2 = {r_squared:.2f}$')

# Label the axes
plt.xlabel('Microbiome Diversity Index')
plt.ylabel('BMI')

# Title and legend
plt.title('Linear Regression of BMI on Microbiome Diversity Index')
plt.legend()

# Show the plot
plt.show()
