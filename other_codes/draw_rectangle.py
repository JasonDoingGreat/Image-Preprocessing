#coding=utf-8

import cv2

f_anno_lines=open("annotation_train.txt").readlines()
line_index=0
for f_anno_line in f_anno_lines:
	f_anno_line_split=f_anno_line.strip().split()
	image_name=f_anno_line_split[0]
	img=cv2.imread(image_name)
	label=""
	for i in range((len(f_anno_line_split)-1)/5):
		xmin=abs(int(f_anno_line_split[1+i*5]))
		ymin=abs(int(f_anno_line_split[2+i*5]))
		xmax=abs(int(f_anno_line_split[3+i*5]))
		ymax=abs(int(f_anno_line_split[4+i*5]))
		label=str(f_anno_line_split[5+i*5])
		if label=="0":
			cv2.imwrite("images_rectgle_0/"+str(0)+image_name.split("/")[-1],img[ymin:ymax,xmin:xmax])
		if label=="17":
			cv2.imwrite("images_rectgle_17/"+str(17)+image_name.split("/")[-1],img[ymin:ymax,xmin:xmax])
		if label=="13":
			cv2.imwrite("images_rectgle_13/"+str(13)+image_name.split("/")[-1],img[ymin:ymax,xmin:xmax])
	line_index+=1
	print line_index
