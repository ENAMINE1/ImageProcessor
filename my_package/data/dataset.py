# Imports
import jsonlines
from PIL import Image
import os
import numpy as np

import urllib.request


class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''

    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        f = jsonlines.open(annotation_file)
        self.annotations = list(f)
        self.transforms = transforms

    def __len__(self):
        '''
            return the number of data points in the dataset
        '''
        return len(self.annotations)

    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        return self.annotations[idx]

    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        im = Image.open(path)
        if self.transforms != None:
            for t in self.transforms:
                im = t.__call__(im)

        return im
        # for t in self.transforms:
        #     if t.__class__ == BlurImage:
        #         im = t.__call__(im)
        #     elif t.__class__ == CropImage:
        #         im = t.__call__(im)
        #     elif t.__class__ == FlipImage:
        #         im = t.__call__(im)
        #     elif t.__call__(im) == RandomCrop:
        #         im = t.__call__(im)
        #     elif t.__class__ == RescaleImage:
        #         im = t.__call__(im)
        #     elif t.__class__ == RotateImage:
        #         im = t.__call__(im)
        # return im
