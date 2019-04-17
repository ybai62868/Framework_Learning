import os
import os.path as osp
import pickle
import mmcv
import numpy as np

data_dir = osp.join('../../../Data','cifar-10-batches-py')
train_output = osp.join('../../../Data', 'raw_train')
test_output = osp.join('../../../Data','raw_test')



def unpickle(file):
    with open(file, 'rb') as fo:
        dict_ = pickle.load(fo, encoding='bytes')
    return dict_

def main():
    flag_train = False
    if flag_train:
        for j in range(1,6):
            data_path = osp.join(data_dir, 'data_batch_' + str(j)) # data_batch_1, data_batch_2, data_batch_3, data_batch_4, data_batch_5
            train_data = unpickle(data_path)
            print(data_path + ' is processing ... ')

            for i in range(10000):
                img = np.reshape(train_data[b'data'][i], (3, 32, 32)).transpose(0, 1, 2)
                label_num = str(train_data[b'labels'][i])
                output_dir = osp.join(train_output, label_num)
                
                if not osp.isdir(output_dir):
                    os.makedirs(output_dir)
                
                img_name = label_num + '_' + str(i + (j - 1) * 10000) + '.png'
                img_path = osp.join(output_dir, img_name)
                mmcv.imwrite(img, img_path)
            print (data_path + 'loaded.')
    else:
        print ('test_batch is processing ...')

        test_data_path = osp.join(data_dir, 'test_batch')
        test_data = unpickle(test_data_path)

        for i in range(10000):
            img = np.reshape(test_data[b'data'][i], (3, 32, 32))
            img = img.transpose(1, 2, 0)

            label_num = str(test_data[b'labels'][i])
            output_dir = osp.join(test_output, label_num)
            
            if not osp.exists(output_dir):
                os.makedirs(output_dir)
            
            img_name = label_num + '_' + str(i) + '.png'
            img_path = osp.join(output_dir, img_name)
            mmcv.imwrite(img, img_path)
        print ('test_batch' + 'loaded.')


if __name__ == '__main__':
    main()