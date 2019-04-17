

import numpy as np
import random
import mmcv


train_txt_path = '../../../Data/train.txt'


def main():
    imgs = np.zeros([32, 32, 3, 1])
    means = []
    stdevs = []
    with open(train_txt_path, 'r') as fout:
        lines = fout.readlines()
        # cnt = len(lines)
        cnt = 500
        for i in range(cnt):
            img_path = lines[i].rstrip().split()[0]
            img = mmcv.imread(img_path)
            img_h, img_w = img.shape[0:2]
            img = mmcv.imresize(img, (img_h, img_w))
            img = img[...,np.newaxis]
            # print (img.shape, imgs.shape)
            imgs = np.concatenate((imgs, img), 3)
    print ('imgs shape =>', imgs.shape)
    imgs = imgs.astype(np.float32)/255.0

    for i in range(3): 
        pixels = imgs[:, :, i, :].ravel()
        print (pixels.shape)
        means.append(np.mean(pixels))
        stdevs.append(np.std(pixels))
    
    means.reverse() # BGR => RGB
    stdevs.reverse()

    print ('NormMean = {}'.format(means))
    print ('NormStd = {}'.format(stdevs))
    print ('torchvision.transforms.Normalize({},{})'.format(means, stdevs))

if __name__ == '__main__':
    main()