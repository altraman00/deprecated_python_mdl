from PIL import Image

# python 对验证码图片进行降噪处理 https://blog.csdn.net/t8116189520/article/details/80342512


# 二值化处理
def two_value():
    img_path = '/Users/knight/Desktop/mobvoi/valid_code/'
    image = Image.open(img_path + 'denoise.png')
    # 灰度图
    lim = image.convert('L')
    # 灰度阈值设为165，低于这个值的点全部填白色
    threshold = 165
    table = []

    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)

    bim = lim.point(table, '1')
    bim.save(img_path + '/denoise/denoise_01.png')


two_value()
