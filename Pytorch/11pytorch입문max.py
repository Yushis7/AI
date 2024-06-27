import torch

a = torch.tensor([[3,1,4],[2,4,5]])
print(a) #기본 값 출력
print(a.shape) #2,3 2차원의 3개의 숫자
print(a.max())  #가장 큰 값 5
print(a.max(dim=0)) 
#3>2 =3 , 1<4 = 4, 4>5 = 5   정리 3,4,5
print(a.max(dim=1)) #1>3>4 = 4 / 2>4>5 = 5 (4,5)
#indices=tensor([2,2])는 3,1,4는 0,1,2순인데 4가 젤 크니 2    2,4,5도 5가 젤 크니 2
#그래서 제일 큰 숫자의 위치가 어디냐? ([2,2])


