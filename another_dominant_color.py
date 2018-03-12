# coding=utf-8
import cv2
import numpy as np
import timeit
import argparse
import matplotlib.pyplot as plt

IMAGE_FILE = 'Images/'


def main(image_file):
    start_time = timeit.default_timer()
    img = cv2.imread(image_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    maxsize = (200,200)
    img = cv2.resize(img,maxsize,interpolation=cv2.INTER_AREA)

    # color = ('r', 'g', 'b')
    # for i, col in enumerate(color):
    #     histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    #     plt.plot(histr, '.', color=col)
    #     plt.xlim([0, 256])
    # plt.show()


    channel_0, channel_1, channel_2 = img[:,:,0].flatten(), img[:,:,1].flatten(), img[:,:,2].flatten()
    channel_0_max = np.argmax(np.bincount(channel_0))
    channel_1_max = np.argmax(np.bincount(channel_1))
    channel_2_max = np.argmax(np.bincount(channel_2))
    # #
    # # channel_list = [channel_0_max, channel_1_max, channel_2_max]
    # #
    # # channel_max_index = channel_list.index(np.max(channel_list))
    # # channel_max = channel_list[channel_max_index]
    #
    height, width, channels = img.shape
    R_list = []
    G_list = []
    B_list = []
    for i in range(height):
        for j in range(width):
            channel_list = list(img[i,j])
            # 特殊情况
            if channel_list[0] == channel_list[1] == channel_list[2]:
                R_list.append(channel_list)
                G_list.append(channel_list)
                B_list.append(channel_list)
                continue
            if channel_list[0] == channel_list[1] and channel_list[0] > channel_list[2]:
                R_list.append(channel_list)
                G_list.append(channel_list)
                continue
            if channel_list[0] == channel_list[2] and channel_list[0] > channel_list[1]:
                R_list.append(channel_list)
                B_list.append(channel_list)
                continue
            if channel_list[1] == channel_list[2] and channel_list[1] > channel_list[0]:
                G_list.append(channel_list)
                B_list.append(channel_list)
                continue

            channel_max_index = channel_list.index(np.max(channel_list))
            if channel_max_index == 0:
                R_list.append(channel_list)
                continue
            if channel_max_index == 1:
                G_list.append(channel_list)
                continue
            if channel_max_index == 2:
                B_list.append(channel_list)
    #
    len_list = [len(R_list), len(G_list), len(B_list)]
    len_max_index = len_list.index(np.max(len_list))
    if len_max_index == 0:
        result_list = [item for item in R_list if item[0] == channel_0_max]
        result = np.sum(result_list, axis=0) / len(result_list)
    if len_max_index == 1:
        result_list = [item for item in G_list if item[1] == channel_1_max]
        result = np.sum(result_list, axis=0) / len(result_list)
    if len_max_index == 2:
        result_list = [item for item in B_list if item[2] == channel_2_max]
        result = np.sum(result_list, axis=0) / len(result_list)

            # if img[i, j, channel_max_index] == channel_max:
            #     result_list.append(img[i,j])

    # result = np.sum(result_list, axis=0) / len(result_list)
    print "Dominant RGB color is:", result

    elapsed = timeit.default_timer() - start_time
    print "Running time is:", elapsed


if __name__ == "__main__":
    # ap = argparse.ArgumentParser()
    # ap.add_argument('-i', '--input_file', help="path to image file")
    # args = vars(ap.parse_args())

    main(IMAGE_FILE + "pic10.jpeg")
    # main(IMAGE_FILE + args["input_file"])

