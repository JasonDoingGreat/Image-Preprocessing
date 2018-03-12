# coding=utf-8
"""
该文件用于从result.txt中提取annotations，并储存于annotation.txt中
"""

import cv2
import time

RESULT_FILE_NAME='_result.txt'
ANNOTATION_FILE_NAME='_annotation.txt'
IMAGE_FILE_NAME = '_images/'

# 定义get annotation函数
def perform(args):
    print "Getting annotation start..."
    start_time=time.time()
    file_lines=open(str(args["task_name"]) + RESULT_FILE_NAME).readlines()
    annotation_file=open(str(args["task_name"]) + ANNOTATION_FILE_NAME,"a")
    line_index=0
    for file_line in file_lines:
        file_line_split=file_line.strip().split()
        img_name=str(args["task_name"]) + IMAGE_FILE_NAME + str(file_line_split[0]).split("/")[-1]
        # print img_name
        img=cv2.imread(img_name)
        if not img is None:
            annotation_file.write(img_name)
            img_h=img.shape[0]
            img_w=img.shape[1]
            for i in range((len(file_line_split)-1)/5):
                pos_y=float(file_line_split[i*5+1])*img_h
                pos_x=float(file_line_split[i*5+2])*img_w
                pos_w=float(file_line_split[i*5+3])*img_w
                pos_h=float(file_line_split[i*5+4])*img_h
                class_name=str(file_line_split[i*5+5])
                x_min=int(pos_x)
                y_min=int(pos_y)
                x_max=int(pos_x+pos_w)
                y_max=int(pos_y+pos_h)
                # print class_name,x_min,y_min,x_max,y_max
                annotation_file.write(" "+str(x_min-5)+" "+str(y_min-10)+" "+str(x_max+5)+" "+str(y_max+5)+" "+str(class_name))
            annotation_file.write("\n")
        line_index+=1
    end_time=time.time()
    annotation_file.flush()
    annotation_file.close()
    print "Process Time:", (end_time - start_time)
    print "Process Time Per Image:", (end_time - start_time) / line_index
    print "Getting annotation done!\n"
