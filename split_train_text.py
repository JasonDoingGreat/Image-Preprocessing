# coding=utf-8
"""
用来分类训练数据集和测试数据集
annotation_train.txt     annotation_test.txt
"""

import random
import os

ANNOTATION_TRAIN_NAME = '_annotation_train.txt'
ANNOTATION_TEST_NAME = '_annotation_test.txt'
NEW_ANNOTATION_NAME = '_new_annotation.txt'

# 读取文件函数
def get_file_lines(file_name):
    if os.path.exists(file_name):
        return open(file_name).readlines()
    else:
        assert "Error: File does not exist!"

# 定义分离数据函数，train和test数据分别存入不同文件
def split_data(args):
    f_annotation_train=open(str(args["task_name"]) + ANNOTATION_TRAIN_NAME,"a")
    f_annotation_test=open(str(args["task_name"]) + ANNOTATION_TEST_NAME,"a")
    file_lines=get_file_lines(str(args["task_name"]) + NEW_ANNOTATION_NAME)
    random.shuffle(file_lines)
    train_size = int(args["ratio"]*len(file_lines))
    file_lines_train=file_lines[0:train_size]
    file_lines_test=file_lines[train_size:]
    for file_lines_train_ in file_lines_train:
        if len(file_lines_train_.strip().split())>1:
            f_annotation_train.write(file_lines_train_.strip()+"\n")
    for file_lines_test_ in file_lines_test:
        if len(file_lines_test_.strip().split())>1:
            f_annotation_test.write(file_lines_test_.strip()+"\n")

