# Lab 15 - Multiple Output Prediction

from torch import nn
import torch

torch.manual_seed(1)

class linear_regression(nn.Module):
    def __init__(self,input_size,output_size):
        super(linear_regression,self).__init__()
        self.linear=nn.Linear(input_size,output_size)
    def forward(self,x):
        yhat=self.linear(x)
        return yhat

model=linear_regression(1,10)
model(torch.tensor([1.0]))

list(model.parameters())
x=torch.tensor([[1.0]])

yhat=model(x)
yhat

X=torch.tensor([[1.0],[1.0],[3.0]])

Yhat=model(X)
Yhat





































