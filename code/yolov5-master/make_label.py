import os
import cv2
import json
train_image_path = '/home/jianpingzhong/data/tianchi_ocr/mchar_train/mchar_train/'
val_image_path = '/home/jianpingzhong/data/tianchi_ocr/mchar_val/mchar_val/'
train_annotation_path = '/home/jianpingzhong/data/tianchi_ocr/mchar_train.json'
val_annotation_path = '/home/jianpingzhong/data/tianchi_ocr/mchar_val.json'
train_data = json.load(open(train_annotation_path))
val_data = json.load(open(val_annotation_path))
label_path = '/home/jianpingzhong/data/tianchi_ocr/coco/labels/'
for key in train_data:
    f = open(label_path+key.replace('.png', '.txt'), 'w')
    img = cv2.imread(train_image_path+key)
    shape = img.shape
    label = train_data[key]['label']
    left = train_data[key]['left']
    top = train_data[key]['top']
    height = train_data[key]['height']
    width = train_data[key]['width']
    for i in range(len(label)):
        x_center = 1.0 * (left[i]+width[i]/2) / shape[1]
        y_center = 1.0 * (top[i]+height[i]/2) / shape[0]
        w = 1.0 * width[i] / shape[1]
        h = 1.0 * height[i] / shape[0]
        # label, x_center, y_center, w, h
        f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
    f.close()
for key in val_data:
    f = open(label_path+'val_'+key.replace('.png', '.txt'), 'w')
    img = cv2.imread(val_image_path+key)
    shape = img.shape
    label = val_data[key]['label']
    left = val_data[key]['left']
    top = val_data[key]['top']
    height = val_data[key]['height']
    width = val_data[key]['width']
    for i in range(len(label)):
        x_center = 1.0 * (left[i]+width[i]/2) / shape[1]
        y_center = 1.0 * (top[i]+height[i]/2) / shape[0]
        w = 1.0 * width[i] / shape[1]
        h = 1.0 * height[i] / shape[0]
        # label, x_center, y_center, w, h
        f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
    f.close()

