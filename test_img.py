#coding=utf-8

import cv2

f_lines=open("annotation_train.txt").readlines()
line_index=0
for f_line in f_lines:
    f_Name=f_line.strip().split()[0]
    img=cv2.imread(f_Name)
    if img==None:
	print "it is error ",line_index+1,f_Name
        import sys
	sys.exit(0)
    line_index+=1
    print line_index



