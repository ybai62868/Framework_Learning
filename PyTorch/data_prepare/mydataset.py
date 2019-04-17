import torch
import mmcv


class MyDataset(torch.utils.data.Dataset):
    def __init__(self, txt_path, transform = None, target_transform = None):
        with open(txt_path, 'r') as fh:
            imgs = []
            for line in fh:
                line = line.rstrip()
                words = line.split()
                imgs.append((words[0], int(words[1])))

            self.imgs = imgs
            self.transform = transform
            self.target_transform = target_transform
    
    def __getitem__(self, index):
        fn, label = self.imgs[index]
        img = mmcv.imread(fn)
        if self.transform is not None:
            img = self.transform(img)
        return img, label
    
    def __len__(self):
        return len(self.imgs)


            