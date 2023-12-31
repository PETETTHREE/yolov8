#---------------------------------------------#
#   运行前一定要修改classes
#   如果生成的2007_train.txt里面没有目标信息
#   那么就是因为classes没有设定正确
#---------------------------------------------#
import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#-----------------------------------------------------#
#   这里设定的classes顺序要和model_data里的txt一样
#-----------------------------------------------------#
# classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes = ["chashugu", "guobaorou", "dongguawanzi", "hongshaodaiyu", "fanqiechaojidan", "mapodoufu", "juanxincairoupian", "youmaicai"]

# E:\python-run-env\Faster-RCNN\VOCdevkit\VOC2007\ImageSets\Main\2007_train.txt

def convert_annotation(year, image_id, list_file):
    in_file = open('E:/code/p/xiao-study/QT-win/Faster-RCNN-FoodDetection/FoodPicture/Annotations/%s.xml'%(year, image_id), encoding='utf-8')
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = 0
        if obj.find('difficult')!=None:
            difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(float(xmlbox.find('xmin').text)), int(float(xmlbox.find('ymin').text)), int(float(xmlbox.find('xmax').text)), int(float(xmlbox.find('ymax').text)))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open(f'E:/code/p/xiao-study/QT-win/Faster-RCNN-FoodDetection/FoodPicture/ImageSets/Main/{year}.txt', encoding='utf-8').read().strip().split()
    list_file = open(f'{year}_{image_set}.txt', 'w', encoding='utf-8')
    for image_id in image_ids:
        list_file.write(f'{wd}/VOCdevkit/VOC{year}/JPEGImages/{image_id}.jpg')
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

