"""This is a simple model of a perceptron based on Nahua Kang's Deep Learning tutorial
on towardsdatascience.com"""

import numpy as np

class SigmoidNeuron:

    def __init__(self, inputs = [1, 1, 1], weights = [6, 2, 2], bias = -5):
        self.sum = 0
        self.bias = bias
        self.inputs = inputs
        self.weights = weights
        self.output = None

    #Summation and bias with sigmoid
    def summation(self):
        inputs = self.inputs
        weights = self.weights

        if len(inputs) == len(weights):
            for x in inputs:
                self.sum = self.sum + (inputs[x] * weights[x])
            z = self.sum + self.bias

        self.sum = 1 / (1 + np.exp(-z))

    #activation function
    def activation(self):
        if self.sum >= .5:
            self.output = 1
        else:
            self.output = 0

s = SigmoidNeuron([1, 0, 0], [6, 2, 2], -5)
s.summation()
s.activation()
print(s.output)