import torch
import torch.nn as nn

def create_model():
    net = nn.Sequential(nn.Linear(100, 10), nn.ReLU(), nn.Linear(10, 1))
    return net
    