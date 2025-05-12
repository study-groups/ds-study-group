import pandas as pd
import altair as alt
import math

# Increase the maximum row limit to 10000
alt.data_transformers.enable(max_rows=None)

# Define the constants
h = 6.626e-34   # Planck's constant
c = 2.998e8     # Speed of light
k = 1.381e-23   # Boltzmann constant

# Define the temperature range
T = [2500, 6000]

# Define the frequency range
nu = [i for i in range(1, int( 14.0e14),  int(1.0e12) )]

# Calculate the spectral radiance for each temperature
B = []
for temp in T:
    B_temp = [(2*h*nu[i]**3)/(c**2 * (math.exp((h*nu[i])/(k*temp)) - 1)) for i in range(len(nu))]
    B.append(B_temp)

# Create a dataframe with the frequency and spectral radiance for each temperature
df = pd.DataFrame({'Frequency (Hz)': nu*len(T), 'Spectral Radiance (W/m^2/Hz)': B[0]+B[1], 'Temperature (K)': [T[0]]*len(nu) + [T[1]]*len(nu)})

# Create a color scale
colors = alt.Scale(
    domain=[T[0], T[1]],
    range=["#e41a1c", "#ff7f00"]
)

# Create a line chart with Vega-Lite
chart = alt.Chart(df).mark_line().encode(
    x='Frequency (Hz)',
    y='Spectral Radiance (W/m^2/Hz)',
    color=alt.Color('Temperature (K)', scale=colors),
    tooltip=['Temperature (K)', 'Frequency (Hz)', 'Spectral Radiance (W/m^2/Hz)']
).properties(
    title='Rayleigh-Jeans Curve and Planck\'s Law',
    width=800,
    height=400
).configure(background='#444')

# Display the chart
chart.show()
