# coding=utf-8

'''

85000次迭代

测试
classes_list: 包 大衣 裤装 上衣 连衣裙 针织衫 卫衣 棉衣 半身裙 鞋子 夹克 风衣 T恤 西服 衬衫
predict_error_num: 17	12	21	26	29	17	2	1	17	19	13	4	14	3	10
predict_no_num:    70	17	40	73	19	9	7	5	23	46	23	15	19	12	17
predict_right_num: 119	27	158	28	96	25	8	3	43	247	48	8	44	17	20



训练
classes_list: 包 大衣 裤装 上衣 连衣裙 针织衫 卫衣 棉衣 半身裙 鞋子 夹克 风衣 T恤 西服 衬衫
predict_error_num: 28	12	65	23	11	11	0	2	34	87	8	3	7	5	5
predict_no_num:    359	10	103	69	12	38	14	8	53	395	26	9	35	9	18
predict_right_num: 1794	633	1984	580	888	867	242	85	782	2941	672	204	448	267	345

90000次迭代

测试
classes_list: 包 大衣 裤装 上衣 连衣裙 针织衫 卫衣 棉衣 半身裙 鞋子 夹克 风衣 T恤 西服 衬衫
predict_error_num:    13	12	19	27	29	16	4	1	14	20	11	3	16	6	15   
predict_no_num:    	  71	13	39	72	17	8	5	6	25	43	23	15	19	12	15   
predict_right_num:    118	31	159	29	98	26	10	2	41	250	48	8	44	17	22   




95000次迭代

测试
classes_list: 包 大衣 裤装 上衣 连衣裙 针织衫 卫衣 棉衣 半身裙 鞋子 夹克 风衣 T恤 西服 衬衫
predict_error_num: 14	9	20	26	30	14	3	1	16	19	17	7	17	4	10   
predict_no_num:    67	19	39	72	17	9	5	5	25	58	22	14	19	13	16   
predict_right_num: 122	25	159	29	98	25	10	3	41	235	49	9	44	16	21  

'''

import os
import argparse
import cv2


# 获取每一行数据的结果
def getFileLines(file_name):
    if os.path.exists(file_name):
        return open(file_name).readlines()
    else:
        assert "error"


"""
混淆矩阵:可视化正确错误率，和错误原因
 0 1 2 3 
0
1
2
3
计算各个数目

接收参数
混淆矩阵,输入的的lines为 1 2 ，  2 2，  3 3，这种形式
"""


def getConfusion_Matrix(file_lines, class_num):
    confusion_Matrix = [[0] * class_num for i in range(class_num)]
    for file_line in file_lines:
        f_line_split = file_line.strip().split()
        # print f_line_split
        confusion_Matrix[int(f_line_split[0])][int(f_line_split[1])] += 1
    return confusion_Matrix


"""
线性数组,检测正确和检测错误，针对每个类别，被检测为错的类别的计数、漏检测技术和被检测为正确的计数
predict_error_num:检测错误技术
predict_no_num:漏检测错误

"""
# 定义预测正确和预测错误的文件


CLASSES = ('0', '1', '2', '3', '4', '5',
           '6', '7', '8')

f_no_wrong_predict = "no_wrong_picture/"
no_wrong_predict = open("no_wrong.txt", "a")


def getArray(test_file_lines, predict_file_lines, class_num):
    test_file_lines = test_file_lines
    test_file_split_array = [test_file_line.strip().split() for test_file_line in test_file_lines]
    predict_file_split_array = [predict_file_line.strip().split() for predict_file_line in predict_file_lines]
    line_index = 0
    predict_error = []
    predict_no = []
    predict_right = []
    for line_k, test_file_split_array_ in enumerate(test_file_split_array):
        test_class = []
        predict_class = []
        for i in range((len(test_file_split_array_) - 1) / 5):
            test_class.append(test_file_split_array_[5 + i * 5])
        test_class = list(set(test_class))
        for i in range((len(predict_file_split_array[line_index]) - 1) / 1):
            predict_class.append(predict_file_split_array[line_index][1 + i * 1])
        predict_class = list(set(predict_class))

        # print test_class,predict_class
        for i in test_class:
            if not i in predict_class:
                predict_no.append(int(i))
        # 预测结果在原始标签中和预测结果不在原始标签中

        for i in predict_class:
            if i in test_class:
                predict_right.append(int(i))
            else:
                predict_error.append(int(i))
        line_index += 1
        print line_index
    predict_error_num = [0] * class_num
    predict_no_num = [0] * class_num
    predict_right_num = [0] * class_num
    # 计算每一类的结果
    for i in predict_error:
        predict_error_num[i] += 1
    for i in predict_no:
        predict_no_num[i] += 1
    for i in predict_right:
        predict_right_num[i] += 1
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


# print predict_error,predict_no




if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-input1", "--inputTestFile", help="path to the input file")
    ap.add_argument("-input2", "--inputPredictFile", help="path to the input file")
    args = vars(ap.parse_args())
    print "main function"
    getArray(getFileLines(args["inputTestFile"]), getFileLines(args["inputPredictFile"]), 9)
    '''
	matrix=getConfusion_Matrix(getFileLines(args["inputTestFile"]),15)
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print str(matrix[i][j])+"\t",
		print "\n"
	'''
