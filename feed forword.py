import numpy as np

# Define the sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define the derivative of the sigmoid function
def sigmoid_derivative(x):
    return x * (1 - x)

# Define the feedforward neural network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights and biases randomly
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))
    
    def forward(self, X):
        # Forward pass through the network
        self.hidden_sum = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.activated_hidden = sigmoid(self.hidden_sum)
        self.output_sum = np.dot(self.activated_hidden, self.weights_hidden_output) + self.bias_output
        self.prediction = sigmoid(self.output_sum)
        return self.prediction
    
    def backward(self, X, y, output):
        # Backward pass through the network
        error = y - output
        output_delta = error * sigmoid_derivative(output)
        
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.activated_hidden)
        
        # Update weights and biases
        self.weights_hidden_output += self.activated_hidden.T.dot(output_delta)
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True)
        self.weights_input_hidden += X.T.dot(hidden_delta)
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True)
    
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch}, Loss: {loss:.4f}")
    
    def predict(self, X):
        return np.round(self.forward(X))

# Example usage:
if __name__ == "__main__":
    # Example dataset (XOR problem)
    X = np.array([[0, 0],
                  [0, 1],
                  [1, 0],
                  [1, 1]])
    y = np.array([[0],
                  [1],
                  [1],
                  [0]])
    
    # Initialize and train the neural network
    input_size = X.shape[1]
    hidden_size = 4
    output_size = y.shape[1]
    nn = NeuralNetwork(input_size, hidden_size, output_size)
    nn.train(X, y, epochs=10000)
    
    # Predict on new data
    test_input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    predictions = nn.predict(test_input)
    print("\nPredictions:")
    for i in range(len(test_input)):
        print(f"Input: {test_input[i]}, Predicted Output: {predictions[i]}")
