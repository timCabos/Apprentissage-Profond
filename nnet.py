import numpy as np
import scipy.special

class Nnet:

    mutation_rate = 0.05

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

        def breed(self, nn):
            #Fonction de breed
            return child

        def mutate(self):
            for x in np.nditer(self, op_flags=["readwrite"]):
                if random.random() < mutation_rate:
                    #Suite
