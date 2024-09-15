import pandas as pd
import numpy as np
n = 100 # rows
m = 4   # cols
df = pd.DataFrame(np.random.randint(0,100,size=(n,m)))
df.columns=list('abcd') # features a, b, c, and d
mask= [0]*n # list of 100 zeros
# we need to make entries bool and set some to true
mask[1]= 1;
mask[3]= 1;
# use a generator to generate 
bm=[True if x==1 else False for x in mask] 
# show fist 5 of bm list
type(bm) # list
bm[:5]
# select rows only when boolean mask is True
df[bm]
# create a list of random integers from 0 to n-1
random = [np.random.randint(0,n-1) for x in mask]
# create a list of bools from random list
randomMask=[1 if x > n/2 else 0 for x in random]
# select random rows from data frame
df[randomMask]

