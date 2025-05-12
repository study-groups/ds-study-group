import pandas as pd
import numpy as np
n = 100
m = 4 
# Generate A matrix using generators. Create n number
# of row vectors m elements long
A = [[0]* m for i in range(n)] # A is right shape to loop over

df = pd.DataFrame(np.random.randint(0,100,size=(n,m)))
df.columns=list('abcd') # features a, b, c, and d
