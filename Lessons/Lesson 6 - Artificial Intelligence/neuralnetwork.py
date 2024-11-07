import numpy as np

# Data
x = np.array(([0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]), dtype=float)
y = np.array(([0], [1], [1], [0], [1], [0], [0], [1]), dtype=float)
xPredicted = np.array(([0, 0, 1]), dtype=float)

# Normalize data
x = x / np.amax(x, axis=0)
xPredicted = xPredicted / np.amax(xPredicted, axis=0)

# Open loss file
lossFile = open("SumSquaredLossList.csv", "w")


class Neural_Network(object):
    def __init__(self):  # Fixed constructor method
        self.inputLayerSize = 3
        self.outputLayerSize = 1
        self.hiddenLayerSize = 4
        self.W1 = np.random.rand(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.rand(self.hiddenLayerSize, self.outputLayerSize)

    def feedForward(self, x):
        self.z = np.dot(x, self.W1)
        self.z2 = self.activationSigmoid(self.z)
        self.z3 = np.dot(self.z2, self.W2)
        o = self.activationSigmoid(self.z3)
        return o

    def backwardPropagate(self, x, y, o):
        self.o_error = y - o
        self.o_delta = self.o_error * self.activationSigmoidPrime(o)
        self.z2_error = self.o_delta.dot(self.W2.T)
        self.z2_delta = self.z2_error * self.activationSigmoidPrime(self.z2)
        self.W1 += x.T.dot(self.z2_delta)
        self.W2 += self.z2.T.dot(self.o_delta)

    def trainNetwork(self, x, y):
        o = self.feedForward(x)
        self.backwardPropagate(x, y, o)

    def activationSigmoid(self, s):
        return 1 / (1 + np.exp(-s))

    def activationSigmoidPrime(self, s):
        return s * (1 - s)

    def saveSumSquaredLossList(self, i, error):
        lossFile.write(str(i) + "," + str(error.tolist()) + '\n')

    def saveWeights(self):
        np.savetxt("weightsLayer1.txt", self.W1, fmt="%s")
        np.savetxt("weightsLayer2.txt", self.W2, fmt="%s")

    def predictOutput(self):
        print("Predicted XOR output data based on trained weights:")
        print("Expected (X1-X3):\n" + str(xPredicted))
        print("Output (Y1):\n" + str(self.feedForward(xPredicted)))


# Initialize and train the neural network
myNeuralNetwork = Neural_Network()
trainingEpochs = 1000

for i in range(trainingEpochs):
    print("Epoch #" + str(i) + "\n")
    print("Network Input:\n" + str(x))
    print("Expected Output of XOR Gate Neural Network:\n" + str(y))

    # Get network output and calculate loss
    actual_output = myNeuralNetwork.feedForward(x)
    print("Actual Output from XOR Gate Neural Network:\n" + str(actual_output))
    Loss = np.mean(np.square(y - actual_output))

    # Save loss and train
    myNeuralNetwork.saveSumSquaredLossList(i, Loss)
    print("\n")
    myNeuralNetwork.trainNetwork(x, y)

# Save weights, close file, and make prediction
myNeuralNetwork.saveWeights()
lossFile.close()  # Closing the file
myNeuralNetwork.predictOutput()  # Fixed method call spelling
