# -*- coding: UTF-8 -*-

from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("logs")

image_path = "dataset/train/0002_1621693143.jpg"
# image_path = "/Users/mobvoi/workspace/sourceTree/mdl/python/pytorch/learn_pytorch_01/dataset/train/0002_1621693143.jpg"

img_pil = Image.open(image_path)

img_array = np.array(img_pil)

print(type(img_array))
print(img_array.shape)

writer.add_image("train", img_array, 2, dataformats='HWC')

writer.close()
