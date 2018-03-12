# coding=utf-8
import os
import cv2
import random


bool_list = [True, False]


def check_image_none():
    data_path = "texture"
    class_list = os.listdir(data_path)
    for class_name in class_list:
        class_path = os.path.join(data_path, class_name)
        image_list = os.listdir(class_path)
        for image_name in image_list:
            image_path = os.path.join(class_path, image_name)
            img = cv2.imread(image_path)
            if img is None:
                print image_path
                os.remove(image_path)


def aug_delete(class_path, num):
    image_list = os.listdir(class_path)
    delete_image_list = random.sample(image_list, num)
    for d_image_name in delete_image_list:
        image_path = os.path.join(class_path, d_image_name)
        os.remove(image_path)


def aug(class_path, num):
    image_list = os.listdir(class_path)
    image_list = random.sample(image_list, num)
    for image_name in image_list:
        image_path = os.path.join(class_path, image_name)
        for aug_num in range(1):
            img = cv2.imread(image_path)
            height, width, _ = img.shape
            # 随机水平翻转图像
            if random.choice(bool_list):
                img = cv2.flip(img, 1)
            # 随机剪裁图像
            down_ratio = random.uniform(0, 0.15)
            up_ratio = random.uniform(0.85, 1)
            y_min = int(down_ratio * height)
            y_max = int(up_ratio * height)
            x_min = int(down_ratio * width)
            x_max = int(up_ratio * width)
            img = img[y_min: y_max, x_min: x_max]
            cv2.imwrite(image_path[:-4] + "_" + str(aug_num) + ".jpg", img)


def main():
    data_path = "texture"
    class_list = os.listdir(data_path)
    for class_name in class_list:
        print class_name
        class_path = os.path.join(data_path, class_name)
        if class_name == "条纹":
            aug_delete(class_path, 3900)
        if class_name == "花纹":
            aug_delete(class_path, 4800)
        if class_name == "蕾丝":
            aug_delete(class_path, 4200)
        if class_name == "动物纹":
            aug_delete(class_path, 600)
        if class_name == "格纹":
            aug_delete(class_path, 3100)
        if class_name == "几何纹":
            aug_delete(class_path, 300)


if __name__ == "__main__":
    main()
    # check_image_none()
