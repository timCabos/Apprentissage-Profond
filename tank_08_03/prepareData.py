import numpy as np
import scipy.special
from param import *

bullets_normalizer=[1, window_length, window_height, bullet_speed, bullet_speed]

def data(x1,x2,y1,y2,l1,l2,b1,b2):
    inputs =[x1/window_length ,y1/window_height, x2/window_length ,y2/window_height, l1/life_tot ,l2/life_tot ]   #Normalisation des inputs
    for i in range (max_bullet) :
        for j in range (5) :
            inputs.append(b1[i][j]/bullets_normalizer[j])
            inputs.append(b2[i][j]/bullets_normalizer[j])
    #inputs_m = np.array(inputs, ndmin=2).T
    return inputs
