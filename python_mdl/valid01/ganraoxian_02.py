from PIL import Image
from PIL.ImageEnhance import Color


def ganraoxian(img, savePath):  # img：图片地址
    # img = Image.open('/home/yang/png/'+str(i)+'.png') # 读入图片
    width = img.size[0]
    heigth = img.size[1]  # 获取长宽
    smap = {}
    slist = []
    keylist = []
    for i in range(0, width):
        for j in range(0, heigth):
            argb = img.getpixel((i, j))
            r = argb[0]
            g = argb[1]
            b = argb[2]
            sum = r + g + b  # 得到每一点的rgb

            if sum not in smap.keys():  # 如果没有该sum值的点  进行添加  并且给值为1
                smap[sum] = 1
            else:
                num = smap[sum]
                smap[sum] = num + 1  # 如果有了这个值  在原基础上+1
    slist = sorted(smap.items(), key=lambda x: x[1], reverse=False)

    if (len(slist) > 4):
        num1 = slist[len(slist) - 5][1]
        num2 = slist[len(slist) - 4][1]
        num3 = slist[len(slist) - 3][1]
        num4 = slist[len(slist) - 2][1]  # 获取像素点最多的四个点

        for key in smap:
            if smap[key] == num1 or smap[key] == num2 or smap[key] == num3 or smap[key] == num4:
                # if num1 in smap or num2 in smap or num3 in smap or num4 in smap :
                keylist.append(key)  # 找到对应颜色的点

    for x in range(0, width):
        for y in range(0, heigth):
            argb = img.getpixel((x, y))
            r = argb[0]
            g = argb[1]
            b = argb[2]
            ssum = r + g + b
            flag = True
            for i in range(1, 3):  # px+1
                if y + i < heigth and y - i > 0 and x - i > 0 and x + i < width:

                    upargb = img.getpixel((x, y - i))
                    endargb = img.getpixel((x, y + i))
                    rightupargb = img.getpixel((x + i, y + i))
                    leftupargb = img.getpixel((x - i, y + i))
                    leftdownargb = img.getpixel((x - i, y - i))
                    rightdownargb = img.getpixel((x + i, y - i))
                    r1 = upargb[0]
                    g1 = upargb[1]
                    b1 = upargb[2]
                    sum1 = r1 + g1 + b1

                    r2 = endargb[0]
                    g2 = endargb[1]
                    b2 = endargb[2]
                    sum2 = r2 + g2 + b2

                    r3 = rightupargb[0]
                    g3 = rightupargb[1]
                    b3 = rightupargb[2]
                    sum3 = r3 + g3 + b3

                    r4 = leftupargb[0]
                    g4 = leftupargb[1]
                    b4 = leftupargb[2]
                    sum4 = r4 + g4 + b4

                    r5 = leftdownargb[0]
                    g5 = leftdownargb[1]
                    b5 = leftdownargb[2]
                    sum5 = r5 + g5 + b5

                    r6 = rightdownargb[0]
                    g6 = rightdownargb[1]
                    b6 = rightdownargb[2]
                    sum6 = r6 + g6 + b6
                    if sum1 in keylist or sum2 in keylist or sum3 in keylist or sum4 in keylist or sum5 in keylist or sum6 in keylist:
                        flag = False
            if (ssum not in keylist and flag):
                img.putpixel((x, y), (255, 255, 255))
    for x in range(0, width):
        for y in range(0, heigth):
            if img.getpixel((x, y)) == (255, 255, 255, 255):
                continue
            else:
                img.putpixel((x, y), (0, 0, 0, 255))
                # curImg.setRGB(x, y, Color.white.getRGB())
    img.save(savePath)


if __name__ == '__main__':
    imgPath  = '/Users/knight/Desktop/mobvoi/valid_code/denoise_val/verifycode_01.png'
    savePath = '/Users/knight/Desktop/mobvoi/valid_code/denoise_val/verifycode_02.png'
    img = Image.open(imgPath)
    ganraoxian(img, savePath)
