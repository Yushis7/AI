import torch

#mean = 평균값
a=torch.FloatTensor([[1,2,3],[4,5,6]])
print(a)
print(a.mean())
print(a.mean(dim=0))
print(a.mean(dim=1))
