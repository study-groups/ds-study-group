import numpy as np
import matplotlib.pyplot as plt

class PicoMC:
    def __init__(self, data_x, data_y):
        self.data_x = np.array(data_x)
        self.data_y = np.array(data_y)
        self.n_data = len(data_y)
        self.trace = None
    
    def likelihood(self, params):
        beta_0, beta_1, sigma = params
        y_pred = beta_0 + beta_1 * self.data_x
        residual = self.data_y - y_pred
        return -0.5 * np.sum((residual / sigma) ** 2) - (self.n_data / 2) * np.log(2 * np.pi * sigma ** 2)
    
    def prior(self, params):
        beta_0, beta_1, sigma = params
        # Normal priors for beta_0 and beta_1, half-normal for sigma
        return -0.5 * (beta_0 / 10) ** 2 - 0.5 * (beta_1 / 10) ** 2 - np.log(sigma if sigma > 0 else np.inf)
    
    def posterior(self, params):
        return self.likelihood(params) + self.prior(params)
    
    def metropolis_hastings(self, initial_params, n_iterations, step_size):
        current_params = initial_params
        self.trace = [current_params]
        for _ in range(n_iterations):
            proposal = np.random.normal(current_params, step_size)
            p_accept = min(1, np.exp(self.posterior(proposal) - self.posterior(current_params)))
            if np.random.rand() < p_accept:
                current_params = proposal
            self.trace.append(current_params)
        self.trace = np.array(self.trace)
    
    def traceplot(self):
        fig, axs = plt.subplots(3, figsize=(10, 7))
        params = ['beta_0', 'beta_1', 'sigma']
        for i in range(3):
            axs[i].plot(self.trace[:, i])
            axs[i].set_title(f'Trace for {params[i]}')
        plt.tight_layout()
        plt.show()
    
    def summary(self):
        print("Parameter Estimates:")
        means = np.mean(self.trace, axis=0)
        stds = np.std(self.trace, axis=0)
        for i, param in enumerate(['beta_0', 'beta_1', 'sigma']):
            print(f"{param}: mean = {means[i]:.2f}, std = {stds[i]:.2f}")
    
    def check_convergence(self):
        # A simple convergence check: compare the variance of the first half of the trace to the second half
        # This is a very basic check; in practice, more sophisticated methods like Gelman-Rubin should be used
        variances_first_half = np.var(self.trace[:len(self.trace)//2], axis=0)
        variances_second_half = np.var(self.trace[len(self.trace)//2:], axis=0)
        print("Convergence Check:")
        for i, param in enumerate(['beta_0', 'beta_1', 'sigma']):
            ratio = variances_first_half[i] / variances_second_half[i]
            print(f"{param}: variance ratio (first half to second half) = {ratio:.2f}")

