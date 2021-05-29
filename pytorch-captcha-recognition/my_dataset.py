# -*- coding: UTF-8 -*-
import os
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
from PIL import Image
import one_hot_encoding as ohe
import captcha_setting


# 继承了抽象类Dataset
# Dataset抽象类， 所有自定义的Dataset都需要继承它，并且必须复写__getitem__()这个类方法
class mydataset(Dataset):

    def __init__(self, folder, transform=None):
        self.train_image_file_paths = [os.path.join(folder, image_file) for image_file in os.listdir(folder)]
        self.transform = transform

    def __len__(self):
        return len(self.train_image_file_paths)

    # 重写__getitem__()方法，__getitem__方法的是Dataset的核心，作用是接收一个索引， 返回一个样本
    def __getitem__(self, idx):
        # 从train_image_file_paths中根据idx获取图片样本
        image_root = self.train_image_file_paths[idx]
        image_name = image_root.split(os.path.sep)[-1]
        image_mark_name = image_name.split('_')[0]
        image = Image.open(image_root)
        if self.transform is not None:
            # 在这里做transform，转为tensor等等
            image = self.transform(image)
        label = ohe.encode(image_name.split('_')[0])
        # 为了方便，在生成图片的时候，图片文件的命名格式 "4个数字或者数字_时间戳.PNG", 4个字母或者即是图片的验证码的值，字母大写,同时对该值做 one-hot 处理
        return image, label, image_mark_name


# 图像预处理模块transforms，主要包括下面的方法：
# 数据中心化，数据标准化，缩放，裁剪，旋转，翻转，填充，噪声添加，灰度变换，线性变换，仿射变换，亮度、饱和度及对比度变换。
transform = transforms.Compose([
    # transforms.ColorJitter(),
    transforms.Grayscale(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])


def get_train_data_loader():
    dataset = mydataset(captcha_setting.TRAIN_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=64, shuffle=True)


def get_test_data_loader():
    dataset = mydataset(captcha_setting.TEST_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)


def get_predict_data_loader():
    dataset = mydataset(captcha_setting.PREDICT_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)
