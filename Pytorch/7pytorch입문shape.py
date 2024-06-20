import torch

a = torch.tensor([1,2,3,4])
x = a.shape  #torch의 갯 수(사이즈)를 알려줌
print(x)  

b= torch.ones([3,4,5,5,5])
y = b.shape  #torch.tensor 아니고 torch.ones 하면 정수 다 보여줌
print(y)


