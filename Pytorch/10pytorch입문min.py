import torch

a = torch.tensor([[3,1,4],[2,4,5]])
print(a) #기본 값 출력
print(a.shape) #2,3 2차원의 3개의 숫자
print(a.min())  #가장 작은 숫자 값
print(a.min(dim=0)) 
#디멘션 중 가장 작은 값3,2 중 작은 값 2/ 1,4중 작은 값 1 /4,5중 작은 값 4
print(a.min(dim=1)) #3,1,4중 가장 작은 값 1 , 2,4,5중 가장 작은 값 2

