import torch

a = torch.rand(3,20,50) # [M,N,K]
b = torch.rand(3,20,50) # [M,N,K]

output1 = torch.cat([a,b],dim = 0 ) #[M+M , N , K]
print(output1.shape)
print(a)
print(b)
print(output1)
