import os
import shutil
train_image_path = '/home/jianpingzhong/data/tianchi_ocr/mchar_train/mchar_train/'
val_image_path = '/home/jianpingzhong/data/tianchi_ocr/mchar_val/mchar_val/'
dst_image_path = '/home/jianpingzhong/data/tianchi_ocr/coco/images/'
train_image_list = os.listdir(train_image_path)
val_image_list = os.listdir(val_image_path)
for img in train_image_list:
    shutil.copy(train_image_path+img, dst_image_path+img)
for img in val_image_list:
    shutil.copy(val_image_path+img, dst_image_path+'val_'+img)
