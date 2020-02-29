import numpy as np
import scipy.special

def data(x1,x2,y1,y2,l1,l2,b1,b2):
    inputs =[x1,y1,x2,y2,l1,l2]
    for i in range (4) :
        for j in range (5) :
            inputs.append(b1[i][j])
            inputs.append(b2[i][j])
    #inputs_m = np.array(inputs, ndmin=2).T
    return inputs
