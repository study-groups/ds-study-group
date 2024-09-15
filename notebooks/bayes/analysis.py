# This is the analysis.py file
import numpy as np

from pico_mc import PicoMC
from data import microbiome_diversity_index, BMI

# Instantiate PicoMC with the imported data
pico_mc = PicoMC(microbiome_diversity_index, BMI)

# Initial parameter guesses and MCMC settings
initial_params = [np.mean(BMI), 0, 1]  # [beta_0, beta_1, sigma]
n_iterations = 100000
step_size = [0.2, 0.1, 0.1]

# Run the sampler
pico_mc.metropolis_hastings(initial_params, n_iterations, step_size)

# Traceplot and summary
pico_mc.check_convergence()
pico_mc.traceplot()
pico_mc.summary()
