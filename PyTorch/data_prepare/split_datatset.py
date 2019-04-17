import os
import os.path as osp
import glob
import random
import shutil

dataset_root = osp.join('../../../Data','raw_test')
train_dir = osp.join('../../../Data', 'train')
valid_dir = osp.join('../../../Data', 'val')
test_dir = osp.join('../../../Data', 'test')

ratio = [0.8, 0.1, 0.1]

assert sum(ratio) == 1

def main():
    for root, dirs, files in os.walk(dataset_root):
        for sDir in dirs:
            imgs_list = glob.glob(osp.join(root, sDir) + '/*.png') 
            random.seed(233)
            random.shuffle(imgs_list)
            cnt = len(imgs_list)

            train_point = int(cnt * ratio[0])
            valid_point = int(cnt * (ratio[0] + ratio[1]))

            # file_list =  [train_dir, valid_dir, test_dir]
            # for item in file_list:
            #     if not osp.exists(item):
            #         os.makedirs(item)

            for i in range(cnt):
                if i < train_point:
                    out_dir = osp.join(train_dir, sDir)
                elif i < valid_point:
                    out_dir = osp.join(valid_dir, sDir)
                else:
                    out_dir = osp.join(test_dir, sDir)
                
                out_path = osp.join(out_dir,osp.split(imgs_list[i])[-1])
                
                if not osp.exists(out_dir):
                    os.makedirs(out_dir)

                shutil.copy(imgs_list[i], out_path)
            print('Class: {}, train: {}, valid: {}, test: {}'.format(sDir, train_point, valid_point, cnt-valid_point))


if __name__ == '__main__':
    main()