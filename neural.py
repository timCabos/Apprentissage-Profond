# Importing everything
import os
import keras
from keras import *
from keras.optimizers import Adam, Nadam
from keras.models import Sequential
from keras.layers import Dense, Dropout, AlphaDropout
from keras.layers import Dense
import numpy
import time
import pandas
from sklearn.metrics import confusion_matrix, cohen_kappa_score
import matplotlib.pyplot as plt
from jeutimh import *

#Entrees
model = Sequential()
model.add(Dense())

#Sorties
