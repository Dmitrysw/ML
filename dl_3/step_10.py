import torch.nn as nn


def create_conv_model():
    return nn.Sequential(
        nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, padding=1),
        nn.ReLU(),

        nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
        nn.ReLU(),

        nn.MaxPool2d(kernel_size=2),

        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),
        nn.ReLU(),

        nn.MaxPool2d(kernel_size=2),

        nn.Conv2d(in_channels=128, out_channels=128, kernel_size=1),
        nn.ReLU(),

        nn.Flatten(),
        nn.Linear(128 * 7 * 7, 512),
        nn.LeakyReLU(),
        nn.Linear(512, 10)
    )