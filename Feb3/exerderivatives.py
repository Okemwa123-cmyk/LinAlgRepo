import torch

x=torch.tensor(2.0,requires_grad = True)
y=torch.tensor(1.0,requires_grad = True)
z=torch.tensor(2.0,requires_grad = True)

f=-5*x**2 + 4*x**2
f.backward()
print(x.grad)
print(y.grad)
print(z.grad)