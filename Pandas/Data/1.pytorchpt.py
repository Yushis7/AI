import torch

##1.초기화 되지 않은 텐서
# x= torch.empty(4,2)
# print(x)

##2.무작위로 초기화된 텐서
# x=torch.rand(2,2)
# print(x)

##3.데이터타입(dtype)이 long이고,0으로 채워진 텐서
# x = torch.zeros(4,2,dtype=torch.long)
# print(x)

##4.사용자가 입력한 값으로 텐서 초기화
# x = torch.tensor([3,2.3])
# print(x)

##5.2 x 4 크기, double 타입, 1로 채워진 텐서
x = torch.tensor(())  # Initialize x as an empty tensor 
x = x.new_ones(2, 4, dtype=torch.double)
print(x)

##6. x와 같은 크기 float 타입 무작위로 채워진 텐서
x= torch.randn_like(x,dtype=torch.float) #기존에 있던 tensor x랑 같은 걸 만들어달란 randn_like
print(x)

##7 텐서의 크기 계산
print(x.size())
