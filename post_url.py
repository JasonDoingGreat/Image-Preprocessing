#coding=utf-8
import urllib2
from urllib2 import urlopen
import numpy as np
import json
import time
import cv2
import argparse

#post方式访问serving,post传送的数据未post形式
def http_post(url,data):  
	json_data = json.dumps(data)
	req = urllib2.Request(url, json_data)
	response = urllib2.urlopen(req)
	return response.read() 
 
def create_opencv_image_from_url(url, cv2_img_flag=3):
	print("create_opencv_image_from_url")
	request = urlopen(url)
	img_array = np.asarray(bytearray(request.read()), dtype=np.uint8)
	return cv2.imdecode(img_array, cv2_img_flag)


if __name__=="__main__":

	url='http://192.168.48.16:8000'
	f_lines=open("Polo 衫审核结果情况.tsv").readlines()
	right_num=0
	wrong_num=0
	f_new=open("f_new_9_09.txt","a")
	"""
	5140	3976	1164
	"""
	for line_index,f_line in enumerate(f_lines[1:]):
		f_line_split=f_line.strip().split()
		imageUrl=f_line_split[0]
		print imageUrl
		f_new.write(imageUrl)
		data = {"imageUrl": imageUrl,"sizeFilterThres":"0.005"}
		start_time=time.time()

		#解析serving返回的数据并打印
		resp = list(json.loads(http_post(url,data)))
		label_list=[]
		for i in range(len(resp)):
			label_list.append(resp[i]['tag'])

		f_new.write(" "+str(label_list)+"\n")
		
		print line_index+1,right_num,wrong_num,label_list,f_line_split[1]
	print right_num,wrong_num




