import torch

a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([[5,6],[7,8]])

print(a.add(b))  #a+b 
print(a)    #a+b = a
print(a.add_(b))  #add_를 붙여 a를 1,2,3,4에서 6,8,10,12로 바뀜 
print(a)   #add_a는 기존 a와 달라진 값을 출력한다


