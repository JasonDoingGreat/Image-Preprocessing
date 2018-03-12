# coding=utf-8
'''
该文件用于平衡图片数量，并对图片做相应修改
'''

from __future__ import print_function

import cv2


FILE_NAME = "_annotation.txt"
NEW_FILE_NAME = "_new_annotation.txt"
ANNOTATION_TRAIN_NAME = "_annotation_train.txt"
LABEL_FILE_NAME = "_label_class.txt"
ANNOTATION_BALANCE_NAME = "_annotation_balance.txt"

# 编辑图片亮度
def brightness(img_name, brightness_value):
   # BGR格式转换为HSV格式
   image=cv2.imread(img_name)
   print('images brightness:')
   hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
   height, width, channels = hsv.shape	
   for x in range(height):
      for y in range(width):
         if hsv[x,y,2] + brightness_value > 255:
            hsv[x,y,2] = 255
         elif hsv[x,y,2] + brightness_value < 0:
            hsv[x,y,2] = 0
         else:
            hsv[x,y,2] += brightness_value
         # 添加新的像素通道值
   edit_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
   return edit_img


# 编辑图片对比度
def contrast(img_name, contrast_value):
   print('image contrast:')
   image=cv2.imread(img_name)
   height, width, channels = image.shape	
   for x in range(height):
      for y in range(width):
         for c in range(channels):
            if image[x,y,c] + contrast_value > 255:
               image[x,y,c] = 255
            elif image[x,y,c] + contrast_value < 0:
               image[x,y,c] = 0
            else:
               image[x,y,c] += contrast_value
   return image


# 镜像处理图片
def flip_img(img_name):
   img=cv2.imread(img_name)
   iLR=cv2.flip(img,90)
   return iLR


# 平滑滤波
def blur_img(img_name):
   img=cv2.imread(img_name)
   blur=cv2.blur(img,(5,5))
   return blur


# 中值滤波
def media_blur(img_name):
   img=cv2.imread(img_name)
   blur=cv2.medianBlur(img,5)
   return blur


# 平衡数据量
def perform(args, file_name,class_list):
    f_balance=open(str(args["task_name"]) + ANNOTATION_BALANCE_NAME,"a")
    file_lines=get_file_lines(file_name)
    line_index=0

    for file_line in file_lines:
        f_balance.write(file_line)
        file_line_split=file_line.strip().split()
        file_line_split_len=(len(file_line_split)-1)/5

        for i in range(file_line_split_len):
            class_num=int(file_line_split[5+i*5])
            if class_num in class_list:
                img_name=str(file_line_split[0])
                img=cv2.imread(img_name)
                # print(img_name)
                img_w=img.shape[1]
                img_h=img.shape[0]
                new_file_line=img_name
                # 对图片做镜像处理
                for i in range(file_line_split_len):
                    recogn=abs(int(file_line_split[i*5+3])-int(file_line_split[i*5+1]))
                    new_file_line=new_file_line+" "+str(abs(int(file_line_split[i*5+1])-img_w)-recogn)+" "+file_line_split[5*i+2]+" "+str(abs(int(file_line_split[i*5+3])-img_w)+recogn)+" "+file_line_split[5*i+4]+" "+file_line_split[5*i+5]
                    # print("-----"+file_line_split[i*5+1]+" "+file_line_split[5*i+2]+" "+file_line_split[i*5+3]+" "+file_line_split[5*i+4]+" "+file_line_split[5*i+5]+" "+str(img_w))
                new_img_name=img_name.replace(str(args["task_name"]) + "_images/", str(args["task_name"]) + "_images/f1_")
                cv2.imwrite(new_img_name,flip_img(img_name))
                f_balance.write(new_file_line.replace(str(args["task_name"])    +"_images/",str(args["task_name"])+"_images/f1_") + '\n')
           #if class_num==0 or class_num==2:
	       #  new_img_name=img_name.replace("images/","images/f2_")
           #  cv2.imwrite(new_img_name,flipImg(img_name))
           #  f_balance.write(new_fileLine.replace("images/","images/f2_")+"\n")
           #  new_img_name=img_name.replace("images/","images/f3_")
           #  cv2.imwrite(new_img_name,flipImg(img_name))
           #  f_balance.write(new_fileLine.replace("images/","images/f3_")+"\n")
        line_index+=1
        print(line_index)
    #print class_num_list
    print("Balanced ruhan data!")


# 获取所有文件行数
def get_file_lines(file_name):
    return open(file_name).readlines()


# 从文件中读取标签类别，存储到dictionary
def get_class_label_dict(args):
    file_name = str(args["task_name"]) + LABEL_FILE_NAME
    class_label_dict={}
    file_lines=get_file_lines(file_name)
    for file_line in file_lines:
        file_line=file_line.strip().split(":")
        print(file_line)
        class_label_dict[str(file_line[0])]=int(file_line[1])
    print("Getting class label dictionary done!\n")
    return class_label_dict


# 获取每个类别的图片数目
def get_annotation_class_num(args,class_label_dict, target_file_name):
    class_num=[0]*len(class_label_dict)
    file_lines=get_file_lines(str(args["task_name"]) + target_file_name)
    for file_line in file_lines:
        f_line=file_line.strip().split()
        for i in range((len(f_line)-1)/5):
            class_num[class_label_dict[f_line[5+i*5]]] += 1
    return class_num


# 将中文标签替换为数字标签
def replace_lable_to_num(args, class_label_dict):
    new_file_name = str(args["task_name"]) + NEW_FILE_NAME
    file_name = str(args["task_name"]) + FILE_NAME
    new_file=open(new_file_name,"a")
    file_lines=get_file_lines(file_name)
    line_index=0
    for file_line in file_lines:
        if not "其他上装" in file_line:
            new_file_line=file_line
            for key in class_label_dict.keys():
                if key in file_line:
                    new_file_line=new_file_line.replace(str(key),str(class_label_dict[key]))
            new_file.write(new_file_line)
        line_index+=1
        # print(line_index)
    new_file.flush()
    new_file.close()
    print('Replacing labels done!')
