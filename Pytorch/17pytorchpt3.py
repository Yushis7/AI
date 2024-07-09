import torch

#0 dimension
# t0 = torch.tensor([])
# print(t0.ndim)
# print(t0.shape)
# print(t0)

#1 dimension
# t1 = torch.tensor([1,2,3])
# print(t1.ndim)
# print(t1.shape)
# print(t1)

#2 dimension
# t2 = torch.tensor([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])
# print(t2.ndim)
# print(t2.shape)
# print(t2)


#3 dimension
t3 = torch.tensor([[[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                   [[1,2,3],
                   [4,5,6],
                   [7,8,9]],
                   [[1,2,3],
                   [4,5,6],
                   [7,8,9]]])

print(t3.ndim)
print(t3.shape)
print(t3)


#4차원은 컬러이미지 데이터가 대표적 (흑백은 3차원 가능) 주로 samples,height,width,(color)channel을 가진다

#5차원은 비디오 데이터가 대표적 samples,height,width,(color)channel,frames가진 구조로 사용

