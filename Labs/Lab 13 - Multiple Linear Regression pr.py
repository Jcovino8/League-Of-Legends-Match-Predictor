# Lab 13 - Multiple Linear Regression prediction

# Import the libraries and set the random seed

from torch import nn
import torch
torch.manual_seed(1)

# Set the weight and bias

w = torch.tensor([[2.0], [3.0]], requires_grad=True)
b = torch.tensor([[1.0]], requires_grad=True)

# Define Prediction Function

def forward(x):
    yhat = torch.mm(x, w) + b
    return yhat

# Calculate yhat

x = torch.tensor([[1.0, 2.0]])
yhat = forward(x)
print("The result: ", yhat)

# Sample tensor X

X = torch.tensor([[1.0, 1.0], [1.0, 2.0], [1.0, 3.0]])

# Make the prediction of X 

yhat = forward(X)
print("The result: ", yhat)

# Make a linear regression model using build-in function

model = nn.Linear(2, 1)


# Make a prediction of x

yhat = model(x)
print("The result: ", yhat)


# Make a prediction of X

yhat = model(X)
print("The result: ", yhat)

# Create linear_regression Class

class linear_regression(nn.Module):
    
    # Constructor
    def __init__(self, input_size, output_size):
        super(linear_regression, self).__init__()
        self.linear = nn.Linear(input_size, output_size)
    
    # Prediction function
    def forward(self, x):
        yhat = self.linear(x)
        return yhat

model = linear_regression(2, 1)


# Practice: Build a model to predict the follow tensor.

X = torch.tensor([[11.0, 12.0, 13, 14], [11, 12, 13, 14]])
model = linear_regression(4, 1)
yhat = model(X)
print("The result: ", yhat)

















