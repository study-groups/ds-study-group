#! python3
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def plotDemo():
    fig,ax = plt.subplots() 
    ax.plot([1,2,3,4], [1,4,2,3])
    plt.savefig(sys.stdout.buffer)

if __name__=='__main__':
    plotDemo()
