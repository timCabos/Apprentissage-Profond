
import numpy as np
import scipy.special
import random
from param import *

class Nnet:

    def __init__(self, num_input, num_hidden_1, num_hidden_2 , num_hidden_3, num_output):
        self.num_input = num_input
        self.num_hidden_1 = num_hidden_1
        self.num_hidden_2 = num_hidden_2
        self.num_hidden_3 = num_hidden_3
        self.num_output = num_output
        self.weight_input_hidden1 = np.random.uniform(-0.5, 0.5, size=(self.num_hidden_1, self.num_input))
        self.weight_hidden1_hidden2 = np.random.uniform(-0.5, 0.5, size=(self.num_hidden_2, self.num_hidden_1))
        self.weight_hidden2_hidden3 = np.random.uniform(-0.5, 0.5, size=(self.num_hidden_3, self.num_hidden_2))
        self.weight_hidden3_output = np.random.uniform(-0.5, 0.5, size=(self.num_output, self.num_hidden_3))
        self.activation_function = lambda x: scipy.special.expit(x)

    def get_outputs(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden1_inputs = np.dot(self.weight_input_hidden1, inputs)
        hidden1_outputs = self.activation_function(hidden1_inputs)
        hidden2_inputs = np.dot(self.weight_hidden1_hidden2, hidden1_outputs)
        hidden2_outputs = self.activation_function(hidden2_inputs)
        hidden3_inputs = np.dot(self.weight_hidden2_hidden3,hidden2_outputs)
        hidden3_outputs = self.activation_function(hidden3_inputs)
        final_inputs = np.dot(self.weight_hidden3_output, hidden3_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs



#GENERATIONS OF NEURAL NETWORKS
def darwin(tab, score):                    #Selection function , split list in good and bad
    max_1=score.index(max(score))
    score[max_1]=0
    max_2=score.index(max(score))
    good_boys=[tab(max_1),tab(max_2)]
    del tab[max_1:max_2]                # Delete good ones
    bad_boys=tab
    return good_boys , bad_boys



def breed(nn1, nn2):                            #breeding function , random weights from each neural net selected
    num_rows = nn1.shape[0]
    num_cols = nn2.shape[1]
    child = nn1
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            if random.random() < 0.5 :
                child[i][j] = nn2[i][j]
    return child

def mutate(tab):
    for x in np.nditer(tab, op_flags=["readwrite"]):
        if random.random() < mutation_chance :
            x[...] = np.random.random_sample() - 0.5
