from PIL import Image

# 去除干扰线
im = Image.open('/Users/knight/Desktop/mobvoi/valid_code/denoise/denoise_01.png')
# 图像二值化
data = im.getdata()
w, h = im.size
black_point = 0

for x in range(1, w - 1):
    for y in range(1, h - 1):
        mid_pixel = data[w * y + x]  # 中央像素点像素值
        if mid_pixel < 10:  # 找出上下左右四个方向像素点像素值
            top_pixel = data[w * (y - 1) + x]
            left_pixel = data[w * y + (x - 1)]
            down_pixel = data[w * (y + 1) + x]
            right_pixel = data[w * y + (x + 1)]

            # 判断上下左右的黑色像素点总个数
            if top_pixel < 10:
                black_point += 1
            if left_pixel < 10:
                black_point += 1
            if down_pixel < 10:
                black_point += 1
            if right_pixel < 10:
                black_point += 1
            if black_point < 1:
                im.putpixel((x, y), 255)
            # print(black_point)
            black_point = 0

im.save('/Users/knight/Desktop/mobvoi/valid_code/denoise/denoise_02.png')
