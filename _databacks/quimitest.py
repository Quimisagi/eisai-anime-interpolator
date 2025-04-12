# quimi_dataset.py
import os
import numpy as np
from PIL import Image  # Replace with your actual image loader (e.g., `I()` from _util)

class QuimiTest:
    def __init__(self, path, split='all'):
        self.path = path
        self.split = split
        self.bns = np.array(self.get_bns(), dtype=np.unicode_)
    
    def __len__(self):
        return len(self.bns)
    
    def __getitem__(self, idx):
        if isinstance(idx, int):
            bn = str(self.bns[idx])
        elif isinstance(idx, str):
            bn = idx
        else:
            raise ValueError(f"Invalid index: {idx}")
        
        full_path = os.path.join(self.path, bn)
        return {
            'bn': bn,
            'images': [
                Image.open(os.path.join(full_path, f"{frame}.png"))
                for frame in ['prev', 'curr', 'next']
            ],
        }
    
    def get_bns(self):
        split_dirs = []
        if self.split in ['train', 'all']:
            train_dir = os.path.join(self.path, 'train')
            split_dirs += [f"train/{dn}" for dn in os.listdir(train_dir)
                           if os.path.isdir(os.path.join(train_dir, dn))]
        if self.split in ['test', 'all']:
            test_dir = os.path.join(self.path, 'test')
            split_dirs += [f"test/{dn}" for dn in os.listdir(test_dir)
                           if os.path.isdir(os.path.join(test_dir, dn))]
        return sorted(split_dirs)
