import pandas as pd
import altair as alt
import math

# Define the constants
h = 6.626e-34   # Planck's constant
m = 9.11e-31   # Mass of the particle (electron)
L = 1e-9        # Length of the box (1 nm)
T = int(1.0e7)        # Temperature of the system (in Kelvin)
T = int(6.0e3)        # Temperature of the system (in Kelvin)

# Define the number of energy levels
N =100 

# Calculate the energy levels and probabilities
#convert to eV
E = [((n**2) * (h**2) / (8*m*L**2))/(1.6e-19) for n in range(0, N)]
Z = sum([math.exp(-E[i]/(8.617e-5*T)) for i in range(N)])
P = [math.exp(-E[i]/(8.617e-5*T))/Z for i in range(N)]

# Create a dataframe with the energy levels and probabilities
df = pd.DataFrame({'Energy Level (eV)': E, 'Probability': P})
df['Energy Level'] = range(N)

# Create a line chart with Vega-Lite

   # y=alt.Y('Energy Level (eV)', axis=alt.Axis(title='eV')),
chart = alt.Chart(df).mark_line().encode(
    x=alt.X('Energy Level', axis=alt.Axis(title='Energy Level')),
    y=alt.Y('Probability', axis=alt.Axis(title='Probability')),
).properties(
    title='Discrete Boltzmann Distribution'
)

# Display the chart
chart.show()
