import torch

#cat 합치려는 차원을 제외한 나머지 차원을 같은 모양으로 만들어 
#차원의 갯 수는 유지되고 해당 차원 값이 늘어난다

# a = torch.rand(5,24,50) # [M,N,K]
# b = torch.rand(5,24,50) # [M,N,K]

# output1 = torch.cat([a,b],dim = 0 ) #[M+M , N , K]
# print(output1.shape)
# output2 = torch.cat([a,b], dim = 1) #[M , N+N , k]
# print(output2.shape)
# output3 = torch.cat([a,b], dim = 2) # [M,N,K+K]
# print(output3.shape)



a = torch.rand(5,24,50) # [M,N,K]
b = torch.rand(2,24,50) # [M,N,K]

output1 = torch.cat([a,b],dim = 0 ) #[M+M , N , K]
print(output1.shape)  # 0번쨰 위치 5+2는 가능
output2 = torch.cat([a,b], dim = 1) #[M , N+N , k]
print(output2.shape) # 1번쨰 위치 24끼리 더해야하는데 0번쨰 자리 5,2가 달라서 오류

