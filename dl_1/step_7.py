import torch
def function03(x: torch.Tensor, y: torch.Tensor):
    w = torch.rand(x.shape[1], dtype=torch.float32, requires_grad=True)
    y_pred = torch.matmul(x, w)
    MSE = torch.mean((y_pred - y) ** 2)
    print (MSE)
    step_size = 0.01
    step = 1
    while MSE >= 1:
        MSE.backward()
        with torch.no_grad():
            w -= w.grad * step_size
        MSE = torch.mean((torch.matmul(x, w) - y) ** 2)
        w.grad.zero_()
        # print (f"MSE = {MSE}", f"номер шара {step}")
        step += 1
    return w