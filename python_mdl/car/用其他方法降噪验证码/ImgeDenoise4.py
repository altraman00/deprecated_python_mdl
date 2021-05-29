from PIL import Image

# 去除干扰线
im = Image.open('/Users/knight/Desktop/mobvoi/valid_code/denoise/denoise_03.png')
# 图像二值化
data = im.getdata()
w, h = im.size
black_point = 0

for x in range(1, w - 1):
    for y in range(1, h - 1):
        if x < 2 or y < 2:
            im.putpixel((x - 1, y - 1), 255)
        if x > w - 3 or y > h - 3:
            im.putpixel((x + 1, y + 1), 255)

im.save('/Users/knight/Desktop/mobvoi/valid_code/denoise/denoise_03.png')
