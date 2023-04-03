def count_parameters_conv(in_channels: int, out_channels: int, kernel_size: int, bias: bool):
    if bias:
        return (in_channels * (kernel_size ** 2) + 1) * out_channels
    else:
        return (in_channels * (kernel_size ** 2)) * out_channels
