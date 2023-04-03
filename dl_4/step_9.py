import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torch.nn as nn
@torch.inference_mode()
def predict_tta(model: nn.Module, loader: DataLoader, device: torch.device, iterations: int = 2):
    # функция для сырых выходов
    @torch.inference_mode()
    def raw_predict(model: nn.Module, loader: DataLoader, device: torch.device):
        model.to(device)
        model.eval()
        predictions = []
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            output = model(x)
            predictions.append(output)  # без torch.argmax, чтоб были сырые выходы
        return torch.concat(predictions)

    prediction = []

    for i in range(iterations):
        single_prediction = raw_predict(model, loader, device)
        prediction.append(single_prediction)  # лист из тензоров по предсказаниями

    prediction = torch.stack(prediction).mean(dim=0)  # усредняемся по предсказаниям
    prediction = torch.argmax(prediction, dim=1)
    return prediction