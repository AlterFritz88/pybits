import torch
import torch.nn

x = torch.tensor([[10., 20.]])
fc = torch.nn.Linear(2, 3)

w = torch.tensor([[11., 12.], [21., 22.], [31., 32]])
fc.weight.data = w

b = torch.tensor([[31., 32., 33.]])
fc.bias.data = b

# Получим выход fc-слоя:
fc_out = fc(x)

fc_out_alternative = torch.mm(x, w.t()) + b

print(fc_out)
print(fc_out_alternative)

assert fc_out == fc_out_alternative