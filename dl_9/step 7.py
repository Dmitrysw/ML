import torch
import torch.nn as nn
import numpy as np

class Similarity1(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, encoder_states: torch.Tensor, decoder_state: torch.Tensor):


        return torch.matmul(encoder_states, decoder_state)