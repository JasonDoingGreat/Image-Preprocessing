# coding=utf-8
from PIL import Image

image = Image.open("Images/pic6.jpg")

image = image.convert('RGB')
# 生成缩略图，减少计算量，减小cpu压力
image.thumbnail((50, 50))
pixels = list(image.getdata())

max_value = 0
result = None
for item in pixels:
    rgb = [float(x)/256. for x in list(item)]
    max_index = rgb.index(max(rgb))
    min_index = rgb.index(min(rgb))
    score = 0
    if max_index == min_index or rgb[max_index] == rgb[3-max_index-min_index] or rgb[min_index] == rgb[3-max_index-min_index]:
        score = rgb[max_index]
    else:
        score = 0.7 * rgb[max_index] + 0.3 * rgb[3-max_index-min_index]
    if score > max_value:
        max_value = score
        result = item
        print max_value
print result

