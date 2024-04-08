import numpy as np
from typing import List, Tuple

# RNN class
class RNN:
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        self.Wxh = np.random.randn(hidden_dim, input_dim) * 0.01
        self.Whh = np.random.randn(hidden_dim, hidden_dim) * 0.01
        self.Why = np.random.randn(output_dim, hidden_dim) * 0.01
        self.bh = np.zeros((hidden_dim, 1))
        self.by = np.zeros((output_dim, 1))

    def forward(self, inputs: np.ndarray) -> np.ndarray:
        h = np.zeros((self.Whh.shape[0], 1))
        self.inputs = inputs
        self.hiddens = {0: h}

        for i, x in enumerate(inputs):
            h = np.tanh(np.dot(self.Wxh, x) + np.dot(self.Whh, h) + self.bh)
            self.hiddens[i + 1] = h

        y = np.dot(self.Why, h) + self.by
        return y
    
    def backward(self, dloss_dy: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
        dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
        dhnext = np.zeros_like(self.hiddens[0])

        for i in reversed(range(len(self.inputs))):
            dh = np.dot(self.Why.T, dloss_dy) + dhnext
            dtanh = (1 - self.hiddens[i + 1] * self.hiddens[i + 1]) * dh
            dbh += np.sum(dtanh, axis=1, keepdims=True)  # Sum gradients over time steps
            dWxh += np.dot(dtanh, self.inputs[i].reshape(-1, 1))  # Reshape input to match dtanh shape
            dWhh += np.dot(dtanh, self.hiddens[i].T)
            dhnext = np.dot(self.Whh.T, dtanh)
        dby = np.sum(dloss_dy, axis=1, keepdims=True)  # Sum gradients over time steps

        for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
            np.clip(dparam, -5, 5, out=dparam)

        return dWxh, dWhh, dWhy, dbh, dby



# Data generation
def generate_input(freq: float, amp: float, phase: float, duration: float = 0.5, sample_rate: int = 256) -> np.ndarray:
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = amp * np.sin(2 * np.pi * freq * t + phase)
    return signal

def input_generator(frequencies: List[float], amp: float, phase: float, duration: float = 0.5, sample_rate: int = 256) -> Tuple[np.ndarray, int]:
    while True:
        freq = np.random.choice(frequencies)
        signal = generate_input(freq, amp, phase, duration, sample_rate)
        label = frequencies.index(freq)
        yield signal, label

# Softmax function
def softmax(x: np.ndarray) -> np.ndarray:
    e_x = np.exp(x - np.max(x))  # subtract max(x) for numerical stability
    return e_x / e_x.sum(axis=0)

# One-hot encoding
def one_hot_encode(label: int, num_classes: int) -> np.ndarray:
    one_hot = np.zeros(num_classes)
    one_hot[label] = 1
    return one_hot

# Loss function
def compute_loss_and_gradOLD(output: np.ndarray, label: int) -> Tuple[float, np.ndarray]:
    output = softmax(output)
    label_vec = one_hot_encode(label, num_classes=output.shape[0])
    loss = -np.sum(label_vec * np.log(output))
    dloss_dy = output - label_vec  # derivative of cross-entropy loss with softmax
    return loss, dloss_dy

def compute_loss_and_grad(output: np.ndarray, label: int) -> Tuple[float, np.ndarray]:
    output = softmax(output)
    label_vec = one_hot_encode(label, num_classes=output.shape[0])
    loss = -np.sum(label_vec * np.log(output))
    dloss_dy = output - label_vec  # derivative of cross-entropy loss with softmax
    return loss, dloss_dy

# Update function
def update_weights_and_biases(rnn: RNN, gradients: Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray], learning_rate: float = 0.01):
    dWxh, dWhh, dWhy, dbh, dby = gradients
    rnn.Wxh -= learning_rate * dWxh
    rnn.Whh -= learning_rate * dWhh
    rnn.Why -= learning_rate * dWhy
    rnn.bh -= learning_rate * dbh
    rnn.by -= learning_rate * dby

# Training loop
frequencies = [4, 8, 16]
amp = 0.5
phase = 0
input_dim = 1
hidden_dim = 100
output_dim = len(frequencies)

rnn = RNN(input_dim, hidden_dim, output_dim)
generator = input_generator(frequencies, amp, phase)

num_training_steps = 1000
for i in range(num_training_steps):
    signal, label = next(generator)
    signal = signal.reshape(-1, 1, 1)
    output = rnn.forward(signal)
    loss, dloss_dy = compute_loss_and_grad(output, label)
    gradients = rnn.backward(dloss_dy)
    update_weights_and_biases(rnn, gradients)
    if i % 100 == 0:  # print loss every 100 steps
        print(f"Step {i}, Loss: {loss}")

