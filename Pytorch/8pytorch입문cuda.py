import torch

# #cuda로 gpu를 쓸 수 있는가? true
# x = torch.cuda.is_available()
# print(x)

# #gpu이름체크(cuda:0에 연결 된 그래픽 카드 기준)
# y = torch.cuda.get_device_name(device=0)
# print(y)

# #사용 가능 gpu 갯 수 체크
# z = torch.cuda.device_count()
# print(z)

# #텐서를 gpu에서 사용하게 만들기 (두 가지 방법)
# a = torch.tensor([1.,2.,3.,4.,5.]).cuda()
# b = torch.tensor([1.,2.,3.,4.,5.]).to("cuda")
# print(a)
# print(b)

# print(a.to("cuda"))

a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([[5,6],[7,8]])

print(a)
print(b)
print(a+b)  #print(a.add(b))
print(a-b)  #print(a.sub(b))
print(a*b)  #print(a.mul(b))
print(a/b)  #print(a.div(b)) 로도 가능
