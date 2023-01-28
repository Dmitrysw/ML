import torch
def function01(tensor: torch.Tensor, count_over:str) -> torch.Tensor:
    if count_over == "columns":
        return torch.mean(tensor, axis=0)
    elif count_over == "rows":
        return torch.mean(tensor, axis=1)