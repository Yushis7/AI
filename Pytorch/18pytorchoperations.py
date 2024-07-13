import torch
import math

a = torch.rand(1,2)*2 -1 
print(a)
print(torch.abs(a))  #절대값
print(torch.ceil(a)) #올림 내림
print(torch.floor(a))  #ceil에서 0-1 = -1
print(torch.clamp(a,-0.5,0.5)) #최솟값을 -0.5로 고정시킴


# 30:32