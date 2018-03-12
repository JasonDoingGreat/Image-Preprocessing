# coding=utf-8
"""
检查图片文件格式是否能够使用，对不能够使用的格式进行转换
"""

import cv2
import sys

NEW_ANNOTATION_NAME = '_new_annotation.txt'

# 定义执行函数，检查数据格式，并进行转换
def perform(args):
    f_lines = open(str(args["task_name"]) + NEW_ANNOTATION_NAME).readlines()

    for line_index, f_line in enumerate(f_lines):
        img_name = f_line.split()[0]
        img = cv2.imread(img_name)
        if not img is None:
            cv2.imwrite(img_name, img)
        else:
            # print line_index
            sys.exit(0)
        print 'Processed', line_index, 'images!'
    print "Writing images done!\n"
