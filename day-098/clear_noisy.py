#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 闲欢
"""

from PIL import Image, ImageDraw


# 判断噪点,如果确认是噪点,用该点的上面一个点的灰度进行替换
# 根据一个点A的RGB值，与周围的8个点的RBG值比较，设定一个值 N（0 <N <8），当A的RGB值与周围8个点的RGB相等数小于N时，此点为噪点
# x, y: 像素点坐标
# G: 图像二值化阀值
# N: 降噪率 0 < N <8
def get_pixel(image, x, y, G, N):
    # 获取像素值
    L = image.getpixel((x, y))

    # 与阈值比较
    if L > G:
        L = True
    else:
        L = False

    nearDots = 0

    if L == (image.getpixel((x - 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x - 1, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x, y + 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y - 1)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y)) > G):
        nearDots += 1
    if L == (image.getpixel((x + 1, y + 1)) > G):
        nearDots += 1

    if nearDots < N:
        return image.getpixel((x, y - 1))
    else:
        return None


# 降噪
# Z: 降噪次数
def clear_noise(image, G, N, Z):
    draw = ImageDraw.Draw(image)

    for i in range(0, Z):
        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                color = get_pixel(image, x, y, G, N)
                if color is not None:
                    draw.point((x, y), color)


# 二值处理
# 设定阈值threshold，像素值小于阈值，取值0，像素值大于阈值，取值1
# 阈值具体多少需要多次尝试，不同阈值效果不一样
def get_table(threshold=115):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


# 打开原始图片
im = Image.open('vc.png')
# 展示原始图片
im.show()

# 将原始图片灰度化
grey_im = im.convert('L')
# 展示灰度化图片
grey_im.show()
# 保存灰度化图片
grey_im.save('grey.png')

# 打开灰度化图片并进行二值处理
binary_im = Image.open('grey.png').point(get_table(120), "1")
# 展示二值化图片
binary_im.show()
# 保存二值化图片
binary_im.save('binary.png')

# 打开二值化图片
b_im = Image.open('binary.png')
# 将二值化图片降噪
clear_noise(b_im, 50, 4, 4)
# 展示降噪后的图片
b_im.show()
# 保存降噪后的图片
b_im.save('result.png')
