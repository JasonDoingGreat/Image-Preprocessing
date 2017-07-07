f_lines=open("annotation_train.txt").readlines()
f_train=open("train.txt","a")
for f_line in f_lines:
	f_train.write(f_line.strip().split()[0]+"\n")

f_train.close()
print "end--"
