# coding=utf-8
import argparse
import random

f_data = open('result.txt')
f_data2 = open('new_result.txt', 'a')

f_lines = f_data.readlines()
length = len(f_lines)
result = []
for i in range(10):
    x = random.randint(0, length)
    print>>f_data2, f_lines[i]

f_data.close()
f_data2.close()


