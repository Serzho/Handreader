import numpy as np

class Neironet():
    def __init__(self):
        pass
    
    def getField(self, data, mode = 0, letter = -1):
        if(mode == 0):
            print('testing')
        else:
             self.__educating(data, letter)

    def __educating(self, data, letter):
        sigmoid = lambda x: 1 / (1 + np.exp(-x))
        
        created_weights = np.array([])
        train_out = np.array([[letter]]).T
        train_in = []
        weights = []

        for i in range(25):
            for k in range(25):
                train_in.append(float(data[i][k]))

        np.random.seed(1)
        
        try:
            f = open('data.txt', 'r')            
        except FileNotFoundError:
            f = open('data.txt', 'w')
            created_weights = 2 * np.random.random(625) - 1
            for i in range(625):
                f.write(str(created_weights[i]) + '\n')
                print(str(created_weights[i]) + '\n')
            f.close()
            f = open('data.txt', 'r')  
        finally:
            for line in f.readlines():
                weights.append(float(line.rstrip()))
            f.close()

        
        #print(weights)
        #print(train_in)
        train_in = np.array([train_in])
        weights = np.array(weights)

        print(sigmoid(np.dot(train_in, weights)))

        for i in range(20000):
            input_layer = train_in
            #print(input_layer)
            #print(weights)
            outputs = sigmoid(np.dot(input_layer, weights))

            err = train_out - outputs
            adjustments = np.dot(input_layer.T, err * (outputs * (10 - outputs)))

            #print(adjustments)
            weights += adjustments[0]

        print(sigmoid(np.dot(train_in, weights)))

        f = open('data', 'w')
        for i in range(625):
                f.write(str(weights[i]) + '\n')
        f.close()

        
            

'''
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

train_in = np.array([[0,0,1],
                        [1,1,1],
                        [1,0,1],
                        [0,1,1]])

train_out = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1
print(synaptic_weights)

for i in range(20000):
    input_layer = train_in
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = train_out - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (10 - outputs)))

    synaptic_weights += adjustments

print(synaptic_weights)
    
print(outputs)
'''



