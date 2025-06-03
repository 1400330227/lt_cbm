import torch

from lt_cbm.modeling.lt_cbm import LTCBM

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = LTCBM()

model.eval()
with torch.no_grad():
    print(model)
