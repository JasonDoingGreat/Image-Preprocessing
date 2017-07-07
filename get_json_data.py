# coding=utf-8
"""
该文件用于从JSON格式数据文件中提取数据，结果保存在result.txt中
"""

import json
import os

RESULT_FILE_NAME = '_result.txt'

# 获取文件行数
def get_file_lines(file_name):
    if os.path.exists(file_name):
        # print file_name
        return open(file_name).readlines()
    else:
        assert "File does not exist!"

# 提取数据主函数
def perform(args):
    # 读取JSON文件，提取数据，存入output_file中
    file_lines = get_file_lines(args["input_file"])
    result_file = open(str(args["task_name"])+RESULT_FILE_NAME, "a")

    for file_line in file_lines:
        file_content = list(json.loads(file_line.strip().split()[1]))
        result_file.write(file_line.strip().split()[0])
        for i in range(len(file_content)):
            # print file_content[i]['tag'], file_content[i]['pos'],
            result_file.write(" " + str(file_content[i]['pos'][0]) + " " + str(file_content[i]['pos'][1]) + " " + str(
                file_content[i]['pos'][2]) + " " + str(file_content[i]['pos'][3]) + " " + str(
                file_content[i]['tag'].encode('utf-8')))
        result_file.write("\n")
    # 关闭文件
    result_file.close()
    print("Getting JSON data done!\n")
