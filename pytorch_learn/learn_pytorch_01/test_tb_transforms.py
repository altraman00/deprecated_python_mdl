# -*- coding: UTF-8 -*-
from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")

img = Image.open("source/pytorch.jpeg")

print(type(img))

# ToTensor
# 新建一个ToTensor对象
trans_totensor = transforms.ToTensor()
# 调用对象的__call__方法的初始化方法
img_tentor = trans_totensor(img)
writer.add_image('totensor', img_tentor, 1)

# Resize
trans_resize = transforms.Resize((212, 212))
img_resize = trans_resize(img)
img_resize = trans_totensor(img_resize)
writer.add_image('Resize_1', img_resize, 1)
print(img_resize)

# Compose
trans_resize = transforms.Resize((100, 512))
trans_compose = transforms.Compose([trans_resize, trans_totensor])
img_resize_2 = trans_compose(img)
writer.add_image('Resize_2', img_resize_2, 1)

# RandomCrop
trans_random_crop = transforms.RandomCrop(200)
trans_compose_2 = transforms.Compose([trans_random_crop, trans_totensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    writer.add_image('RandomCrop', img_crop, i)

writer.close()
