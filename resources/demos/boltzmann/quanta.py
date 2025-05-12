import pandas as pd
import altair as alt
import math

# Define the constants
h = 6.626e-34   # Planck's constant
m = 1           # Mass of the particle
L = 1           # Length of the box
T = 1           # Temperature of the system

h = 6.626e-34   # Planck's constant
L = 1e-9        # Length of the box (1 nm)
m = 9.11e-31    # Mass of the particle (electron)
c = 2.998e8     # Speed of light
k = 1.381e-23   # Boltzmann constant
T = 10000        # Temperature of the system (in Kelvin)

# Define the number of energy levels
N = 10


# Calculate the energy levels and probabilities
E = [(i**2 * h**2) / (8*m*L**2) for i in range(N)]
Z = sum([math.exp(-E[i]/(k*T)) for i in range(N)])
P = [math.exp(-E[i]/(k*T))/Z for i in range(N)]

# Create a dataframe with the energy levels and probabilities
df = pd.DataFrame({'Energy Level': list(range(N)), 'Probability': P})

# Create a bar chart with Vega-Lite
chart = alt.Chart(df).mark_bar().encode(
    x='Energy Level',
    y='Probability'
).properties(
    title='Discrete Boltzmann Distribution'
)

# Display the chart
chart.show()

