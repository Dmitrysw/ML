import torch
def get_normalize(features: torch.Tensor):
    return (features.mean(dim=(0, 2, 3)), features.std(dim=(0, 2, 3)))