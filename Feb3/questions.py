# Working with the csv file to get data
import torch
import pandas as pd 

df=pd.read_csv('data.csv')
# X=df.drop('Y',axis=1)
# X=df.drop('Y',axis=1).to_numpy()
X=torch.tensor (df.drop('Y',axis=1).to_numpy()).float()
# print (x)
Y=torch.tensor (df['Y'].to_numpy()).float().reshape(-1,1)

# print(Y)

w=torch.tensor([
    [2.0],
    [-2.0]
]).float()

b=torch.tensor([
    [-3.0]
])

Yhat = X@w + b
r = Yhat-Y
SSE = r. T@r
loss =SSE/2
print(loss)


