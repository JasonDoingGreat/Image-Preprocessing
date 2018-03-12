# coding=utf-8

import colorsys
from PIL import Image


def get_dominant_color(image):
    image = image.convert('RGBA')
    # 生成缩略图，减少计算量，减小cpu压力
    image.thumbnail((200, 200))
    max_score = 0
    dominant_color = 0

    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        # 跳过纯黑色
        if a == 0:
            continue
        # 计算颜色饱和度
        saturation = colorsys.rgb_to_hsv(r, g, b)[0]
        print saturation
        # # 计算亮度
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        # # 伸缩颜色饱和度
        y = (y - 16.0) / (235 - 16)
        # # 忽略高亮色
        if y > 0.9:
            continue
        # # 评分
        score = (saturation + 0.1) * count
        #
        if score > max_score:
            max_score = score
            print score
            dominant_color = (r, g, b)

    return dominant_color


def main():
    img = Image.open("Images/pic6.jpg")
    print "Dominant Color RGB is:", get_dominant_color(img)


if __name__ == '__main__':
    main()

