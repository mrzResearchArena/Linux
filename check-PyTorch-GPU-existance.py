import torch

print(torch.cuda.is_available())
print(torch.cuda.device_count())

# Reference: https://chrisalbon.com/deep_learning/pytorch/basics/check_if_pytorch_is_using_gpu/
