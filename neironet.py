
import numpy as np

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




