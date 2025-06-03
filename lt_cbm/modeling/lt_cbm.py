from torch import nn


class LTCBM(nn.Module):
    def __init__(self):
        super().__init__()


    def forward(self,images, texts):
        print(images.shape)