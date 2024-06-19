import torch

a = torch.zeros([3,4,5])
x = torch.ones_like(a)
y = torch.rand([3,3,3])
z = torch.rand_like(y)
z = torch.empty_like(y)
print(z)

