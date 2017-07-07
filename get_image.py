# coding=utf-8
"""
该文件用于从result.txt中获得图片下载地址，并下载图片，保存到images文件中
"""

import requests
from subprocess import call

DOWN_IMAGE_NAME = '_down_img.txt'
RESULT_FILE_NAME = '_result.txt'
IMAGE_FILE_NAME = '_images'

# 定义main函数
def perform(args):
   down_img = open(str(args["task_name"]) + DOWN_IMAGE_NAME, 'a')
   file_lines = open(str(args["task_name"]) + RESULT_FILE_NAME).readlines()
   image_file_name = str(args["task_name"]) + IMAGE_FILE_NAME
   call(['mkdir', image_file_name])
   image_num = 0
   for line_index, file_line in enumerate(file_lines):
      if line_index > -1:
         img_name = str(args["task_name"]) + IMAGE_FILE_NAME + '/' + str(file_line.strip().split()[0]).split("/")[-1]
         url = str(file_line.strip().split()[0])
         r = requests.get(url)
         with open(img_name, "a") as code:
            if r.content != None:
               code.write(r.content)
               # print "got one image"
      line_index += 1
      image_num = line_index
      down_img.write(str(line_index) + " " + file_line)
   print "Got", image_num, "images done!\n"
   down_img.close()
