Here we provide the python code for **log-hyperbolic distribution sampling using CDF inversion**. 

## Usage
To use the code for **log-hyperbolic distribution sampling using CDF inversion**, please put [log_hyperbolic_sampling.py](https://github.com/lijingwang/GEOLSCI-240-ENERGY-240/blob/master/hw1/log_hyperbolic_sampling.py) into your python path. 

If you are using Jupyter Notebook for python, just put the *.py* file in your current *.ipynb* folder. 

The sampler can be used as follows:  
```python
from log_hyperbolic_sampling import *

## Example: 
## Get 1000 samples on Case 2: alpha = 0.5, phi = 1, mu = 1,delta = 1. 
## It should take around 40s
sample_array = log_hyperbolic_sampling(N = 1000, alpha = 0.5, phi = 1, mu = 1, delta = 1)
```
