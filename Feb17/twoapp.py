import torch
import torch.nn as nn
import torch.optim as optim 

torch.manual_seed(1)

X= torch.tensor([
    [2.0],
    [5.0],
    [8.0]

])

Y= torch.tensor([
    [3.0],
    [7.0],
    [1.0]
])

model = nn.Linear(1,1)
criterion =nn.MSELoss() # Calculating the loss
optimizer = optim.SGD(model.parameters(), lr= .01) #updates parameters 

epochs =1000

for epoch in range (epochs):
    Yhat=model(X)
    loss= criterion(Yhat,Y) #calculates loss
    loss.backward()
    optimizer.step()#code that updates weights in the model
    optimizer.zero_grad()

#print(model.weight) #gives you the current value of w
#print(model.bias) #gives you the current value of b

X = torch.tensor ([
    [6.0]
])

X = X@w+b

prediction =model(X)
print(prediction)



