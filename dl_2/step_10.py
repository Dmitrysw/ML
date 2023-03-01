import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

@torch.inference_mode()
def evaluate(model: nn.Module, data_loader: DataLoader, loss_fn):
    model.eval()
    total_loss = []

    for x, y in data_loader:
        output = model(x)
        loss = loss_fn(output, y)
        total_loss.append(loss.item())
    return np.mean(total_loss)