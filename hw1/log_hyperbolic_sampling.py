import numpy as np
from scipy.special import kn
from scipy.integrate import quad
from scipy.optimize import root

# pdf f(x)
def log_hyperbolic_pdf(alpha, phi, mu, delta):
    pdf = lambda x: ((1/((1/phi+1/alpha)*delta*np.sqrt(phi*alpha)*x*kn(1,delta*np.sqrt(phi*alpha))))*
                     np.exp(-0.5*(phi+alpha)*np.sqrt(delta**2+(np.log(x)-mu)**2)+0.5*(phi-alpha)*(np.log(x)-mu)))
    return pdf

# cdf F(x)
def log_hyperbolic_cdf(alpha, phi, mu, delta, lower_bd=0, upper_bd=np.inf):
    pdf = log_hyperbolic_pdf(alpha, phi, mu, delta)
    def cdf(x):
        return quad(pdf, 0, x)[0]
    return cdf

# solve F(x) - y = 0, x = F^{-1}(y)
def inverse_log_hyperbolic_cdf(y, alpha, phi, mu, delta):
    ## cdf: F(x)
    cdf = log_hyperbolic_cdf(alpha, phi, mu, delta)
    
    ## shifted_cdf: F(x)-y
    shifted_cdf = lambda x: cdf(x)-y
    
    ## solve F(x)-y = 0, get x
    solve_root = root(shifted_cdf, 0.01).x[0]
    
    return solve_root


# log hyperbolic sampling 
# --------------------------------------------------------
# Main function, the (only) function you need to run
# --------------------------------------------------------
def log_hyperbolic_sampling(N, alpha, phi, mu, delta, seed = 0):
    '''
    log hyperbolic distribution sampling with CDF inversion 
    
    Args: 
        N: (int) the number of samples
        alpha, phi, mu, delta: (float) parameters from log hyperbolic distribution
        seed: (int) the random seed
    Output:
        x: (np.array) sampling_array with length N. 
    
    Note:  
        For N = 1000, the sampling should be finished around 40s. 
    '''
    
    ## set random seed, default = 0
    np.random.seed(seed)
    
    ## Uniform sampling 
    y = np.random.uniform(size = N)
    x = np.zeros(N)
    
    for i in range(N):
        x[i] = inverse_log_hyperbolic_cdf(y[i], alpha, phi, mu, delta)

    return x