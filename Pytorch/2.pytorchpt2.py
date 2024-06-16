import torch

# ft = torch.FloatTensor([1,2,3])  #floattensor는 32bit다
# print(ft)
# print(ft.dtype)


# print(ft.short())  #int16bit
# print(ft.int())  #int 32bit
# print(ft.long())  #표시는 안되지만 64bit
# print(ft.float()) #애도 64bit 인듯? float이니까 32인가?
# print(ft.double()) # float64bit
# print(ft.half())  #float16bit

x=torch.randn(1)
print(x) #랜덤으로 x값 1번 출력해줘
print(x.item())
print(x.dtype)

#cpu,gpu뭐로 할건지 선택
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)
y = torch.ones_like(x,device=device)
print(y)
x = x.to(device)
print(x)
z = x+y
print(z)
print(z.to('cpu', torch.double))
#x값과 y값을 구해서 z를 만드는데 cpu로만 계산되도록 설정한 것

22:40
