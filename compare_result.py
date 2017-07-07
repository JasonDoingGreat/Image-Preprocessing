# coding=utf-8
import numpy as np
import os

# 获取每一行数据的结果
def get_file_lines(file_name):
    if os.path.exists(file_name):
        return open(file_name).readlines()
    else:
        assert "error"


def compare(file_lines, predict_file_lines, class_num):
    test_file_split_array = [file_line.strip().split() for file_line in file_lines]
    predict_file_split_array = [predict_file_line.strip().split() for predict_file_line in predict_file_lines]
    predict_error = []
    predict_no = []
    predict_right = []
    line_index = 0

    for line_k, test_file_split_array_ in enumerate(test_file_split_array):
        test_class = []
        predict_class = []

        # 提取测试集标签
        for i in range((len(test_file_split_array_) - 1) / 5):
            test_class.append(test_file_split_array_[5 + i * 5])
        test_class = np.array(map(int, list(set(test_class))))
        # print test_class

        # 提取预测结果标签
        for i in range((len(predict_file_split_array[line_index]) - 1) / 1):
            # predict_class = predict_file_split_array[line_index][1 + i * 1]
            predict_class.append(predict_file_split_array[line_index][1 + i * 1])
        predict_class = np.array(map(int, list(set(predict_class))))
        # print predict_class

        # 未预测到的结果
        positions = np.in1d(test_class, predict_class, invert=True)
        predict_no.append(list(test_class[positions]))

        '''
        for i in test_class:
            if not i in predict_class:
                predict_no.append(int(i))
        # 预测结果在原始标签中和预测结果不在原始标签中
        '''

        # 提取预测准确的标签和错误的标签
        positions_true = np.in1d(predict_class, test_class)
        positions_false = np.in1d(predict_class, test_class, invert=True)
        predict_right.append(list(predict_class[positions_true]))
        predict_error.append(list(predict_class[positions_false]))

        '''
        for i in predict_class:
            if i in test_class:
                predict_right.append(int(i))
            else:
                predict_error.append(int(i))
        '''

        line_index += 1
        print line_index

    predict_error_num = [0] * class_num
    predict_no_num = [0] * class_num
    predict_right_num = [0] * class_num

    # 计算每一类的结果
    for i in predict_error:
        for x in i:
            predict_error_num[x] += 1
    for i in predict_no:
        for x in i:
            predict_no_num[x] += 1
    for i in predict_right:
        for x in i:
            predict_right_num[x] += 1
    print "predict_error_num:", predict_error_num
    print "predict_no_num:", predict_no_num
    print "predict_right_num:", predict_right_num
    for i in predict_error_num:
        print i, "\t",
    print "\n"
    for i in predict_no_num:
        print i, "\t",
    print "\n"
    for i in predict_right_num:
        print i, "\t",
    print "\n"

    return


if __name__ == '__main__':
    test_file_name = 'annotation_test.txt'
    predict_file_name = 'f_result_text.txt'
    compare(get_file_lines(test_file_name), get_file_lines(predict_file_name), 9)

