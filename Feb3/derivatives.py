import torch

X= torch.tensor(7.0,requires_grad = True)
f=(X**2 + 1)/(X+5)
f.backward() 
print(X.grad)



