import torch.nn as nn
def create_simple_conv_cifar() -> nn.Module:
    return nn.Sequential(
        nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1),
        nn.BatchNorm2d(32),
        nn.MaxPool2d(2),
        nn.Dropout2d(p=0.2),
        nn.ReLU(),

        nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),
        nn.ReLU(),

        nn.MaxPool2d(2),
        nn.Flatten(),

        nn.Linear(8 * 8 * 64, 1024),
        nn.ReLU(),
        nn.Linear(1024, 10)
    )


