import os
import os.path as osp
import glob


train_txt_path = '../../../Data/train.txt'
train_dir = '../../../Data/train'

valid_txt_path = '../../../Data/valid.txt'
valid_dir = '../../../Data/valid'

def fun(output_path, img_dir):
    with open(output_path, 'w') as fin:
        for root, s_dirs, _ in os.walk(img_dir, topdown=True):
            for sub_dir in s_dirs:
                i_dir = osp.join(root, sub_dir)
                img_list = glob.glob(i_dir + '/*.png')
                for i in range(len(img_list)):
                    if not img_list[i].endswith('png'):
                        continue
                    img_path = img_list[i]
                    label = img_list[i].split('/')[-1].split('_')[0]
                    item = img_path + ' ' + label + '\n'
                    print (item)
                    fin.write(item)
    print ('Done!')


def main():
    fun(train_txt_path, train_dir)
    fun(valid_txt_path, valid_dir)

if __name__ == '__main__':
    main()