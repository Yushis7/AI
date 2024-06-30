import torch

a = torch.tensor([[1,2,3,4],[5,6,7,8]])

# print(a.shape)
# print(a)
# print(a.reshape([4,2]))
# print(a.reshape([1,2,4]))
# print(a.reshape([2,2,2]))
# print(a.reshape([-1,4]))
print(a.reshape([-1,4]).shape)


