import os
import shutil
import random
from tqdm import tqdm


"""
标注文件是yolo格式（txt文件）
训练集：验证集 （8：2） 
"""


def split_img(img_path, label_path, split_list):
    try:  # 创建数据集文件夹
        Data = './ImageSetscalss'
        os.mkdir(Data)

        train_img_dir = os.path.join(Data, 'images', 'train')
        val_img_dir = os.path.join(Data, 'images', 'val')

        train_label_dir = os.path.join(Data, 'labels', 'train')
        val_label_dir = os.path.join(Data, 'labels', 'val')

        os.makedirs(train_img_dir)
        os.makedirs(train_label_dir)
        os.makedirs(val_img_dir)
        os.makedirs(val_label_dir)

    except:
        print('文件目录已存在')

    train_ratio, val_ratio = split_list
    all_img = os.listdir(img_path)
    all_img_path = [os.path.join(img_path, img) for img in all_img]
    train_img = random.sample(all_img_path, int(train_ratio * len(all_img_path)))
    train_label = [toLabelPath(img, label_path) for img in train_img]
    for i in tqdm(range(len(train_img)), desc='train ', ncols=80, unit='img'):
        _copy(train_img[i], train_img_dir)
        _copy(train_label[i], train_label_dir)
        all_img_path.remove(train_img[i])
    val_img = all_img_path
    val_label = [toLabelPath(img, label_path) for img in val_img]
    for i in tqdm(range(len(val_img)), desc='val ', ncols=80, unit='img'):
        _copy(val_img[i], val_img_dir)
        _copy(val_label[i], val_label_dir)


def _copy(from_path, to_path):
    shutil.copy(from_path, to_path)


def toLabelPath(img_path, label_path):
    img = os.path.basename(img_path)
    label = img.split('.jpg')[0] + '.txt'
    return os.path.join(label_path, label).replace('\\', '/')


if __name__ == '__main__':
    img_path = './Images_agu'
    label_path = 'Annotations_agu_txt'
    split_list = [0.8, 0.2]  # 数据集划分比例[train:val]
    split_img(img_path, label_path, split_list)
