
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

    def mutate(tab):
        for x in np.nditer(tab, op_flags=["readwrite"]):
            if random.random() < mutation_chance :
                x[...] = np.random.random_sample() - 0.5

    def modify_weights(self):
        Nnet.mutate(self.weight_input_hidden1)
        Nnet.mutate(self.weight_hidden1_hidden2)
        Nnet.mutate(self.weight_hidden2_hidden3)
        Nnet.mutate(self.weight_hidden3_output)

#GENERATIONS OF NEURAL NETWORKS
def darwin(tab, score):                     #Selection function , split list in good and bad
    max_1=score.index(max(score))
    score[max_1]=0
    max_2=score.index(max(score))
    good_boys=[tab[max_1],tab[max_2]]
    del(tab[max_1])                    # Delete good ones
    if max_1 > max_2 :
        del(tab[max_2])
    else :
        del(tab[max_2-1])
    bad_boys=tab
    return good_boys , bad_boys

def breed(nn1, nn2):                            #breeding function , random weights from each neural net selected
    child = Nnet(nb_input, nb_hidden1, nb_hidden2, nb_hidden3, nb_output)
    weights_child = [child.weight_input_hidden1, child.weight_hidden1_hidden2, child.weight_hidden2_hidden3, child.weight_hidden3_output]
    weights_nn1 = [nn1.weight_input_hidden1, nn1.weight_hidden1_hidden2, nn1.weight_hidden2_hidden3, nn1.weight_hidden3_output]
    weights_nn2 = [nn2.weight_input_hidden1, nn2.weight_hidden1_hidden2, nn2.weight_hidden2_hidden3, nn2.weight_hidden3_output]
    for matrix in range(len(weights_child)):
        for i in range(np.shape(weights_child[matrix])[0]):
            for j in range(np.shape(weights_child[matrix])[1]):
                weights_child[matrix][i][j] = weights_nn1[matrix][i][j]
                if random.random() < 0.5:
                    weights_child[matrix][i][j] = weights_nn2[matrix][i][j]
    return child

def sort_bad(bad_boys):
    del bad_boys[random.randint(0,len(bad_boys)-1)]
#    del bad_boys[random.randint(0,len(bad_boys)-1)]
    for i in range(len(bad_boys)):
        bad_boys[i].modify_weights()
    return bad_boys
