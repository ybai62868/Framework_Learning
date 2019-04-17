import os
import os.path as osp
import glob


train_txt_path = '../../../Data/train.txt'
train_dir = '../../../Data/train'

valid_txt_path = '../../../Data/valid.txt'
valid_dir = '../../../Data/valid'

def fun(output_path, img_dir):
    with open(output_path, 'w') as fin:
        for root, _, _ in os.walk(img_dir, topdown=True):
            print (root, s_dirs)
            for sub_dir in s_dirs:
                i_dir = osp.join(root, sub_dir)
                img_list = glob.glob(img_dir + '/*.png')
                print (img_list)





def main():
    fun(train_txt_path, train_dir)
    fun(valid_txt_path, valid_dir)


if __name__ == '__main__':
    main()