import torch
from torch import nn
def function04(x: torch.Tensor, y: torch.Tensor):
    layer = nn.Linear(in_features=x.shape[1], out_features=1, bias=False)
    y_pred = layer(x).ravel()
    MSE = torch.mean((y_pred - y) ** 2)
    print (MSE)
    step_size = 0.01
    step = 1
    while MSE >= 0.3:
        MSE.backward()
        with torch.no_grad():
            layer.weight -= layer.weight.grad * step_size
        y_pred = layer(x).ravel()
        MSE = torch.mean((y_pred - y) ** 2)
        layer.zero_grad()
        print (f"MSE = {MSE}", f"номер шага {step}")
        step += 1
    return layer