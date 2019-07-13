import numpy as np
from math import *

class Neironet():
    def __init__(self):
        pass
    
    def getField(self, data, mode = 0, letter = -1):
        if(mode == 0):
            print('testing')
        else:
             self.__educating(data, letter)

    def __educating(self, data, letter):
        sigmoid = lambda x: 1 / (1 + exp(-x))
        train_in = []
        weights = []
        train_out = (letter - 40) / 1000
        print(train_out)


        for i in range(25):
            for k in range(25):
                train_in.append(data[i][k])

        try:
            f = open('data', 'r')            
        except FileNotFoundError:
            print("New File")
            f = open('data', 'w')
            created_weights = 2 * np.random.random(625) - 1
            for i in range(625):
                f.write(str(created_weights[i]) + '\n')
                #print(str(created_weights[i]) + '\n')
            f.close()
            f = open('data', 'r')  
        finally:
            for line in f.readlines():
                weights.append(float(line.rstrip()))
            f.close()

        print(train_in)
        print('before educating', sigmoid(np.dot(train_in, weights)))

        print('before educating', weights)
        weights = self.__train(train_in, train_out, weights, 20000)
        print('after educating', weights)

        print('after educating', sigmoid(np.dot(train_in, weights)))
        
        f = open('data', 'w')
        for i in range(625):
                f.write(str(weights[i]) + '\n')
        f.close()

    def __train(self, t_in, t_out, weights, cycles):
        for i in range(cycles):
            weights = self.__iteration(t_in, t_out, weights)

        return weights

    def __iteration(self, t_in, t_out, weights):
        sigmoid = lambda x: 1 / (1 + exp(-x))
        x = 0

        for i in range(625):
            x += weights[i] * t_in[i]
        y = sigmoid(x)

        err = t_out - y
        adjustments  = err * sigmoid(y)
        
        for i in range(625):
            weights[i] += t_in[i] * adjustments

        return weights
            





