# coding=utf-8
"""
调用该文件，执行一系列数据预处理操作
"""

import argparse
import os
import get_json_data
import get_image
import get_annotation
import balance_data
import split_train_text
import write_img

RESULT_FILE_NAME = '_result.txt'
IMAGES_FILE_NAME = '_images'
ANNOTATION_FILE_NAME = '_annotation.txt'
LABEL_FILE_NAME = '_label_class.txt'
NEW_ANNOTATION_NAME = '_new_annotation.txt'
ANNOTATION_TRAIN_NAME = '_annotation_train.txt'
ANNOTATION_TEST_NAME = '_annotation_test.txt'
ANNOTATION_BALANCE_NAME = '_annotation_balance.txt'


def get_class_labels(args):
    file_lines = open(str(args["task_name"]) + RESULT_FILE_NAME).readlines()
    labels = []
    label_dict = {}
    label_file_name = str(args["task_name"]) + LABEL_FILE_NAME
    label_file = open(label_file_name, 'a')
    for line in file_lines:
        line = line.strip().split()
        length = len(line)
        # print line
        for i in range((length - 1) / 5):
            labels.append(line[5+5*i])
    labels = list(set(labels))
    for i in range(len(labels)):
        label_file.write(str(labels[i])+":"+str(i) + '\n')
        label_dict[str(i)] = i
    label_file.close()
    return label_dict


# 定义main函数
def main(args):
    # 调用get_json_data，从JSON格式文件中提取数据
    if not os.path.isfile(str(args["task_name"])+RESULT_FILE_NAME):
        get_json_data.perform(args)
    # 调用get_image，从result.txt中ls下载图片，并写入down_img.txt中
    if not os.path.isdir(str(args["task_name"])+IMAGES_FILE_NAME):
        get_image.perform(args)
    # 调用get_anno_from_result，从result.txt中提取annotation，并写入annotation.txt中
    if not os.path.isfile(str(args["task_name"])+ANNOTATION_FILE_NAME):
        get_annotation.perform(args)
    # 统计类别数量，存储到label_class中
    label_dict = get_class_labels(args)
    # 调用balance_data，完成一些数据的检查和处理
    # 读取class label
    class_label_dict = balance_data.get_class_label_dict(args)
    # 将中文label转换成数字label，存储于new_annotation中
    if not os.path.isfile(str(args["task_name"])+NEW_ANNOTATION_NAME):
        balance_data.replace_lable_to_num(args, class_label_dict)
    # 统一数据格式
    # write_img.perform(args)
    # 将数据集分离成train 和 test
    split_train_text.split_data(args)
    # 输出train数据每一类的数据量，以方便决定是否对training数据进行balance
    class_num = balance_data.get_annotation_class_num(args, label_dict, ANNOTATION_TRAIN_NAME)
    print class_num
    print "输入需要平衡的类别号 (从0开始，以space隔开): "
    user_input = raw_input()
    input_list = user_input.split()
    class_list = [int(x) for x in input_list]
    # 对数量较少的数据进行数据平衡
    balance_data.perform(args, "5_annotation_train.txt", class_list)
    # 输出平衡后的train数据每一类数据量
    new_class_num = balance_data.get_annotation_class_num(args, label_dict, ANNOTATION_BALANCE_NAME)
    print "Class numbers after balance:"
    print new_class_num


# 程序入口，传入参数，调用main函数
if __name__ == '__main__':
    # 定义传入参数
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--task_name", help="path to the input file")
    ap.add_argument("-i", "--input_file", help="path to the input file")
    ap.add_argument("-r", "--ratio", type=float, help="training ratio")
    args = vars(ap.parse_args())

    # 检查是否传入了参数
    if args['task_name'] == None:
        raise ValueError('You must supply the task name with --task_name!')
    if args['input_file'] == None:
        raise ValueError("You must supply the data input with --input_file!")
    if args['ratio'] == None:
        raise ValueError("You must supply the training ratio with --ratio!")

    # 将参数传入main函数
    main(args)
