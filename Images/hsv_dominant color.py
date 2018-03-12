import cv2
import timeit
import numpy as np

black_range_low = np.array([0, 0, 0])
black_range_high = np.array([180, 255, 46])
white_range_low = np.array([0, 0, 180])
white_range_high = np.array([180, 35, 255])
red1_range_low = np.array([0, 43, 46])
red1_range_high = np.array([10, 255, 255])
red2_range_low = np.array([156, 43, 46])
red2_range_high = np.array([180, 255, 255])
orange_range_low = np.array([11, 43, 46])
orange_range_high = np.array([25, 255, 255])
yellow_range_low = np.array([26, 43, 46])
yellow_range_high = np.array([34, 255, 255])
green_range_low = np.array([35, 43, 46])
green_range_high = np.array([99, 255, 255])
blue_range_low = np.array([100, 43, 46])
blue_range_high = np.array([155, 255, 255])


def get_index(color_area):
    index = np.argwhere(color_area==0)
    color_area = np.delete(color_area, index)
    return color_area


def main(image_file, top_k):
    start_time = timeit.default_timer()
    img = cv2.imread(image_file)
    maxsize = (200, 200)
    img = cv2.resize(img, maxsize, interpolation=cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)


    black_area = cv2.inRange(hsv, black_range_low, black_range_high)
    white_area = cv2.inRange(hsv, white_range_low, white_range_high)
    red_area = cv2.inRange(hsv, red1_range_low, red1_range_high) + cv2.inRange(hsv, red2_range_low, red2_range_high)
    orange_area = cv2.inRange(hsv, yellow_range_low, yellow_range_high)
    yellow_area = cv2.inRange(hsv, yellow_range_low, yellow_range_high)
    green_area = cv2.inRange(hsv, green_range_low, green_range_high)
    blue_area = cv2.inRange(hsv, blue_range_low, blue_range_high)

    area_list = [black_area, white_area, red_area, orange_area, yellow_area, green_area, blue_area]

    length_list = [len(get_index(black_area.flatten())),
                   len(get_index(white_area.flatten())),
                   len(get_index(red_area.flatten())),
                   len(get_index(orange_area.flatten())),
                   len(get_index(yellow_area.flatten())),
                   len(get_index(green_area.flatten())),
                   len(get_index(blue_area.flatten()))]

    color_top_k = sorted(zip(length_list, range(len(length_list))), reverse=True)[:top_k]

    for i in range(top_k):
        main_area = area_list[color_top_k[i][1]]
        tmp = cv2.bitwise_and(img, img, mask=main_area)
        column_sum = np.sum(np.sum(tmp ,axis=0),axis=0) / length_list[color_top_k[i][1]]
        print column_sum

    elapsed = timeit.default_timer() - start_time
    print "Running time is:", elapsed

