import numpy as np

# Transfer function
def sigmoid(x, Derivative=False):
    if not Derivative:
        return 1 / (1 + np.exp (-x))
    else:
        out = sigmoid(x)
        return out * (1 - out)
		
class backPropNN:
    """Class defining a NN using Back Propagation"""
    
    # Class Members (internal variables that are accessed with backPropNN.member)
    
    numLayers = 0
    shape = None
    weights = []
    
    # Class Methods (internal functions that can be called)
    
    def __init__(self, numNodes):
        """Initialise the NN - setup the layers and initial weights"""

        # Layer info
        self.numLayers = len(numNodes) - 1
        self.shape = numNodes      

        # Input/Output data from last run
        self._layerInput = []
        self._layerOutput = []
        
        # Create the weight arrays
        for (l1,l2) in zip(numNodes[:-1],numNodes[1:]):
            self.weights.append(np.random.normal(scale=0.1,size=(l2,l1+1)))       
        
    # Forward Pass method
    """Get the input data and run it through the NN"""
    def FP(self, input):

        delta = []
        numExamples = input.shape[0]

        # Clean away the values from the previous layer
        self._layerInput = []
        self._layerOutput = []
        
        for index in range(self.numLayers):
            #Get input to the layer
            if index ==0:
                layerInput = self.weights[0].dot(np.vstack([input.T, np.ones([1, numExamples])]))
            else:
                layerInput = self.weights[index].dot(np.vstack([self._layerOutput[-1],np.ones([1,numExamples])]))

            self._layerInput.append(layerInput)
            self._layerOutput.append(sigmoid(layerInput))
            
        return self._layerOutput[-1].T
            
    # backPropagation method
    def backProp(self, input, target, learningRate = 0.2):
        """Get the error, deltas and back propagate to update the weights"""

        delta = []
        numExamples = input.shape[0]
        
        # First run the network
        self.FP(input)
                 
        # Calculate the deltas for each node
        for index in reversed(range(self.numLayers)):
            if index == self.numLayers - 1:
                # If the output layer, then compare to the target values
                output_delta = self._layerOutput[index] - target.T
                error = np.sum(output_delta**2)
                delta.append(output_delta * sigmoid(self._layerInput[index], True))
            else:
                # If a hidden layer. compare to the following layer's delta
                delta_pullback = self.weights[index + 1].T.dot(delta[-1])
                delta.append(delta_pullback[:-1,:] * sigmoid(self._layerInput[index], True))
                
        # Compute updates to each weight
        for index in range(self.numLayers):
            delta_index = self.numLayers - 1 - index
            
            if index == 0:
                layerOutput = np.vstack([input.T, np.ones([1, numExamples])])
            else:
                layerOutput = np.vstack([self._layerOutput[index - 1], np.ones([1,self._layerOutput[index -1].shape[1]])])

            thisWeightDelta = np.sum(\
                    layerOutput[None,:,:].transpose(2,0,1) * delta[delta_index][None,:,:].transpose(2,1,0) \
                    , axis = 0)
            
            weightDelta = learningRate * thisWeightDelta
            
            self.weights[index] -= weightDelta
            
        return error
		
if __name__ == "__main__":
    	
    '''Input = np.array([[0,0],[1,1],[0,1],[1,0]])
    Target = np.array([[0.0],[0.0],[1.0],[1.0]])

    bpn = backPropNN((2,2,1))

    Error = bpn.backProp(Input, Target)
    Output = bpn.FP(Input)

    print('Input \tOutput \t\tTarget')
    for i in range(Input.shape[0]):
        print('{0}\t {1} \t{2}'.format(Input[i], Output[i], Target[i]))

    maxIterations = 100000
    minError = 1e-5

    NN = backPropNN((2,2,1))

    for i in range(maxIterations + 1):
        Error = NN.backProp(Input, Target)
        if i % 2500 == 0:
            print("Iteration {0}\tError: {1:0.6f}".format(i,Error))
        if Error <= minError:
            print("Minimum error reached at iteration {0}".format(i))
            break
    
    print(NN.FP(Input))'''

    import image_px_data_training_sets as data

    NN = backPropNN((784,15,10))

    Input = data.generate_training_data()
    Target = data.generate_output_data()

    for i in range(10000):
        NN.backProp(Input, Target)
    
    result = NN.FP(data.test_data())

    n=0
    grootste_waarde=0
    A=0
    for g in range(10):
        print(result[0,g], ' --> ',n)
        if grootste_waarde<result[0,g]:
            grootste_waarde=result[0,g]
            A=n
        n+=1


    number_result = np.where(result == np.amax(result))
 
    print('Probabiltiy of number :', np.amax(result))
    print('Guessed number is: ', A)
    
#https://mlnotebook.github.io/post/nn-in-python/


    
    
