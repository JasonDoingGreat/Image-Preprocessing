# coding=utf-8
"""
该文件用于对train 文件生成train.mat用于训练，使用selective_search方法
"""
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import os
import dlib
import scipy.io as sio
import numpy as np
from skimage import io
import time
import imghdr
from subprocess import call


def run_dlib_selective_search(image_name):
    img = io.imread(image_name)
    rects = []
    dlib.find_candidate_object_locations(img,rects,min_size = 1000)
    proposals = []
    for k,d in enumerate(rects):
        temp_list = [d.top(),d.left(),d.bottom(),d.right()]
        proposals.append(temp_list)
    proposals = np.array(proposals)
    return proposals


def perform(anno_train_file, train_mat_file, new_anno_train_file):
    # 定义一些变量
    count = 0
    all_proposals = []
    image_names = []
    length = 0
    if os.path.isfile('proposal_file.txt'):
        # 从上一次中断处恢复
        all_proposals = open('proposal_file.txt').readlines()
        length = len(all_proposals)

    # 打开annotation文件和new_annotation文件
    anno_train = open(anno_train_file)
    new_anno_train = open(new_anno_train_file, "a")
    # 记录单个图片提取proposals处理时间
    f_time = open("f_time.txt", "a")
    # 出现异常时，将已提取的proposals存储到文件
    proposal_file = open("proposal_file.txt", "a")

    try:
        for line in anno_train.readlines():
            start_time=time.time()
            image_file_name = line.strip().split()[0]
            # 检查图片格式是否正确，不正确则忽略
            if imghdr.what(image_file_name) not in ('jpg', 'jpeg', 'png', 'peng'):
                print("图片格式错误! 忽略该图片!")
                continue
            # 检查图片文件大小是否合理，不合理则忽略
            image_size = os.stat(image_file_name).st_size
            if image_size < 10000 or image_size > 10000000:
                print("图片大小错误! 忽略该图片!")
                continue

            # 开始提取proposals
            single_proposal = run_dlib_selective_search(image_file_name)
            print type(single_proposal[0])
            all_proposals.append(single_proposal)
            count = count+1
            end_time=time.time()

            # 将valid图片存入new_annotation_train中，代替annotation_train文件
            new_anno_train.write(line)
            # 写入图片处理时间文件
            f_time.write(str(count)+" "+str(line.strip())+" "+str(end_time-start_time)+"\n")
            f_time.flush()
    except:
        # 出现异常情况时，将提取好的proposals写入proposal文件
        print("出现异常！")
        for item in all_proposals:
            print>>proposal_file, item

    sio.savemat(train_mat_file+'train.mat',mdict={'boxes':all_proposals,'images':image_names})
    obj_proposals = sio.loadmat(train_mat_file+'train.mat')
    print obj_proposals
    # 关闭文件
    anno_train.close()
    new_anno_train.close()
    proposal_file.close()
    f_time.close()
