import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Load the survey data
survey_data = pd.read_csv('ps-7/survey.csv')

def logistic_np(x, beta0, beta1):
    return 1 / (1 + np.exp(-(beta0 + beta1 * x)))

def neg_log_likelihood_np(params, x, y):
    beta0, beta1 = params
    probs = logistic_np(x, beta0, beta1)
    log_likelihood = y * np.log(probs + 1e-9) + (1 - y) * np.log(1 - probs + 1e-9)  # Adding a small constant to avoid log(0)
    return -np.sum(log_likelihood)

# Preparing the data
ages_np = survey_data['age'].to_numpy()
responses_np = survey_data['recognized_it'].to_numpy()

# Initial parameters for optimization
initial_params_np = [0.0, 0.0]

# Minimizing the negative log-likelihood
result_np = minimize(neg_log_likelihood_np, initial_params_np, args=(ages_np, responses_np), method='BFGS')

# Extracting the optimized parameters and covariance matrix
beta0_np, beta1_np = result_np.x
covariance_matrix = np.linalg.inv(result_np.hess_inv)

# Generating a range of ages for plotting the logistic model
ages_plot = np.linspace(min(ages_np), max(ages_np), 100)
probabilities_plot = logistic_np(ages_plot, beta0_np, beta1_np)

# Plotting the logistic model and the survey data
plt.figure(figsize=(10, 6))
plt.plot(ages_plot, probabilities_plot, label='Logistic Model', color='blue')
plt.scatter(ages_np, responses_np, alpha=0.5, label='Survey Data', color='red')
plt.title('Probability of Recognizing "Be Kind Rewind" by Age')
plt.xlabel('Age')
plt.ylabel('Probability of Recognition')
plt.legend()
plt.grid(True)
plt.show()
