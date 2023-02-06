# Imports
from PIL import Image
import random
import time


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if self.crop_type == 'center':
            # ratio of size of new image to original size of image
            frac = (self.shape[0] * self.shape[1]) / (image.size[0] * image.size[1])
            left = image.size[0]*((1-frac)/2)
            upper = image.size[1]*((1-frac)/2)
            right = image.size[0]-((1-frac)/2)*image.size[0]
            bottom = image.size[1]-((1-frac)/2)*image.size[1]
            crop_img = image.crop((left, upper, right, bottom))
        else:
            random.seed = time.time()
            x = random.randint(0, image.size[0]-self.shape[0])
            y = random.randint(0, image.size[1]-self.shape[1])
            crop_img = image.crop((x, y, x+self.shape[0], y+self.shape[1]))
        return crop_img

        
