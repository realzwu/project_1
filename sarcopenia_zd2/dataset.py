import os
from torch.utils.data import Dataset
import numpy as np

## import nifti
class niiDataset(Dataset):
    def __init__(self, image_dir, mask_dir, transform=None):
        self.image_dir = image_dir
        self.mask_dir = mask_dir
        self.transform = transform
        self.images = os.listdir(image_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, index):
        img_path = os.path.join(self.image_dir, self.images[index])
        mask_path = os.path.join(self.mask_dir,self.images[index])

        ##  sometimes it need reshape and broadcast according to its format
        image = np.load(img_path) # .reshape(512,512) # + np.array([0,0])
        mask = np.load(mask_path)

        if self.transform is not None:
            augmentations = self.transform(image=image, mask=mask)
            image = augmentations["image"]
            mask = augmentations["mask"]

        return image, mask

