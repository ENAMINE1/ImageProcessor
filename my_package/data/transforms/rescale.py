# Imports
from PIL import Image


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        w, h = image.size
        if type(self.output_size) != tuple:
            new_h = h*self.output_size
            new_w = w*self.output_size
            new_size = (int(new_w),int(new_h))
            img = image.resize(new_size)
        else:
            img = image.resize(self.output_size)
        return img
