import torch 

print(torch.__version__)

device = "cuda" if (torch.cuda.is_available()) else "cpu"
print(device)
print(torch.cuda.get_device_name(0))



