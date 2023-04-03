import torch
import torch.nn as nn
from torch.utils.data import DataLoader

@torch.inference_mode()
def predict(model:nn.Module, loader: DataLoader, device: torch.device):
    predictions_list = []
    model = model.to(device)
    model.eval()
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        output = model(x)
        predictions_list.append(torch.argmax(output, dim=1))

    predictions_list = torch.cat(predictions_list)

    return predictions_list
