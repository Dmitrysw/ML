import torch
from torch import nn
import numpy as np


def train(model, data_loader, optimizer, loss_fn):
    model.train()
    loss_list = []

    for x, y in data_loader:
        optimizer.zero_grad()

        output = model(x)

        loss = loss_fn(output, y)

        print(f'{loss.item():.5f}')

        loss_list.append(loss.item())

        loss.backward()

        optimizer.step()
    return np.mean(loss_list)