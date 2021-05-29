from PIL import Image
from pytesseract import pytesseract


def two(img, savePath):  # img：图片地址
    i = 0
    # img = Image.open('/home/yang/png/0.png') # 读入图片
    img = img.convert("RGBA")
    while i < 4:  # 循环次数视情况进行调整
        i = i + 1
        pixdata = img.load()
        # 一次二值化

        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][0] < 90:  # 使RGB值中R小于90的像素点变成纯黑
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][1] < 190:  # 使RGB值中G小于90的像素点变成纯黑
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][2] > 0:  # 使RGB值中B大于0的像素点变成纯白
                    pixdata[x, y] = (255, 255, 255, 255)

    # 理论上的二值化代码只有上面那些，RGB值的调整阈值需要针对不同验证码反复调整。同时实际中一组阈值往往没法做到完美，后面的部分是视实际情况添加的类似部分

    # 二次二值化（除去某些R、G、B值接近255的颜色）
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y][0] < 254:
                pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][1] < 254:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)

    # 三次二值化，怼掉纯黄色（实际使用中发现很多图片最后剩几个纯黄色的像素点）
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pixdata[x, y] == (255, 255, 0, 255):
                pixdata[x, y] = (0, 0, 0, 255)

    img.save(savePath)


if __name__ == '__main__':
    imgPath = '/Users/knight/Desktop/mobvoi/valid_code/denoise_val/verifycode_02.png'
    savePath = '/Users/knight/Desktop/mobvoi/valid_code/denoise_val/verifycode_03.png'
    img = Image.open(imgPath)
    two(img, savePath)

    info = Image.open(savePath)
    image_info = pytesseract.image_to_string(info)
    print(image_info)
