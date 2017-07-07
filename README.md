# Image-Preprocessing
This is a repository to store some useful image preprocessing codes (with opencv)

## 数据准备
将所需要处理的JSON数据格式txt文件存放于根目录下，例如abcd.txt.
待处理数据格式为: img_url  [{"tag":"","property":[],"pos":["x1","y1","x2","y2"]}]

## 运行程序
执行main.py文件, 参数包括:
1. task_name: 任务名称
2. input_file: 待处理数据文件
3. ratio: 训练集比例

程序运行提示：
程序运行过程中会要求用户输入类别数字，请根据输出的每一类别数据量，输入所需要平衡的类别即可。以数字输入，空格间隔。（类别从0开始计）

```shell
$ python main.py --task_name=5 --input_file=5_data.txt --ratio=0.8
```

## 程序运行结果：
1. 程序运行过程中，会自动下载图片并存储到"$(task_name)_images/"目录下，同时记录图片下载结果与down_img.txt中。
2. 提取的数据储存于result.txt中。
3. 程序会自动生成$(task_name)_new_annotation.txt和$(task_name)_label_class.txt，分别存储数字化标签的数据文件和标签目录。
4. 运行过程中会输出每一类别数据量，并允许根据观察输入所需要平衡的数据类别，程序会自动平衡所需数据（增加水平翻转图像，后续会添加剪裁图像）
5. 平衡数据后，输出平衡后每一类别数据量。
