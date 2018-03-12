
import cv2
import numpy as np
import timeit
import argparse

IMAGE_FILE = 'Images/'

def main(image_file):
    start_time = timeit.default_timer()
    img = cv2.imread(image_file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    maxsize = (200,200)
    img = cv2.resize(img,maxsize,interpolation=cv2.INTER_AREA)

    channel_0, channel_1, channel_2 = img[:,:,0].flatten(), img[:,:,1].flatten(), img[:,:,2].flatten()
    channel_0_max = np.argmax(np.bincount(channel_0))
    channel_1_max = np.argmax(np.bincount(channel_1))
    channel_2_max = np.argmax(np.bincount(channel_2))

    channel_list = [channel_0_max, channel_1_max, channel_2_max]

    channel_max_index = channel_list.index(np.max(channel_list))
    channel_max = channel_list[channel_max_index]
    print channel_max

    height, width, channels = img.shape
    result_list = []
    for i in range(height):
        for j in range(width):
            if img[i, j, channel_max_index] == channel_max:
                result_list.append(img[i,j])

    result = np.sum(result_list, axis=0) / len(result_list)
    print "Dominant RGB color is:", result

    elapsed = timeit.default_timer() - start_time
    print "Running time is:", elapsed

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input_file', required=True, help="path to image file")
    args = vars(ap.parse_args())

    main(IMAGE_FILE + args["input_file"])

