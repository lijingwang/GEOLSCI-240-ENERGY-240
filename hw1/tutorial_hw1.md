Here we provide the python code for **log-hyperbolic distribution sampling using CDF inversion** and **log-normal distribution sampling**

## Install and Usage
To use the code for sampling, please put the *extreme_value_sampling.py* into your python path. 

If you are using Jupyter Notebook for python, just put the *extreme_value_sampling.py* file in your current *.ipynb* folder. 

The sampler can be used as follows:  
```python
from extreme_value_sampling import *

## Example: 
## Get 1000 samples from log-hyperbolic distribution: phi = 3.61, gamma = 2.12, mu = -0.54, delta = 1.3,. 
## It should take around 10s for 1000 samples. 

sample_array_log_hyper = log_hyperbolic_sampling(N = 1000, phi = 3.61, gamma = 2.12, mu = -0.54, delta = 1.3)

## Get 1000 samples from log-normal distribution: mu = 0, sigma = 1.5 

sample_array_log_normal = log_normal_sampling(N = 1000, mu = 0, sigma = 1.5 )
```
