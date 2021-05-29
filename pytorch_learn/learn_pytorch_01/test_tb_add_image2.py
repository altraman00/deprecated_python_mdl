# -*- coding: UTF-8 -*-

from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

import os

writer = SummaryWriter("logs")

filePath = "dataset/train"

for dirpath, dirname, filenames in os.walk(filePath):
    print(dirpath)
    print(filenames)
    for i, image_name in enumerate(filenames):
        image_path = os.path.join(dirpath, image_name)
        print(str(i) + '-->' + image_path)

        img_pil = Image.open(image_path)
        img_array = np.array(img_pil)
        print(type(img_array))
        print(img_array.shape)

        writer.add_image("train", img_array, i, dataformats='HWC')

writer.close()
