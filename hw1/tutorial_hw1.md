Here we provide the python code for **log-hyperbolic distribution sampling using CDF inversion**. 

## Usage
To use the code for **log-hyperbolic distribution sampling using CDF inversion**, please download [hw1]() and add that into your python path
```python
import sys
sys.path.append('/path/to/hw1')
```

The sampler can be used as follows:  
```python
from log_hyperbolic_sampling import *
## Example: Get 1000 samples on Case 2: alpha = 0.5, phi = 1, mu = 1,delta = 1. 
sample_array = log_hyperbolic_sampling(N = 10, alpha = 0.5, phi = 1, mu = 1,delta = 1)
```