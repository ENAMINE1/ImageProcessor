#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import  Download
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.rotate import RotateImage

import numpy as np
from PIL import Image
import os
#os.environ["CURL_CA_BUNDLE"]=""
idx = 1


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''
    global idx
    if os.path.exists(outputs) == False:
        os.mkdir(outputs)

    # Create the instances of the dataset, download
    dataset = Dataset(annotation_file, transforms)
    download = Download()

    # Print image names and their captions from annotation file using dataset object
    if idx <= 1:
        for d in dataset.annotations:
            print(d['file_name'])
            c = d['captions']
            print('The Captions are : ')
            for j in c:
                print(j['caption'])
            print()

    # Download images to ./data/imgs/ folder using download object
    for img in dataset.annotations:
        download(r'./data/imgs/'+img['file_name'], img['url'])

    # Transform the required image (roll number mod 10) and save it seperately
    img_no = 30047 % 10
    img = dataset.__transformitem__(
        './data/imgs/'+dataset.__getann__(img_no)['file_name'])
    img.save(outputs+'/Transformed_img'+str(idx)+'.jpg')

    # Get the predictions from the captioner for the above saved transformed image
    print()
    print('Captions for Transformed Image '+str(idx)+':')
    d = captioner.__call__(outputs+'/Transformed_img'+str(idx)+'.jpg', 3)
    for i in range(len(d)):
        print(d[i])
    idx +=1
    print()


def main():
    captioner = ImageCaptioningModel()
    # Sample arguments to call experiment()
    experiment(r'./data/annotations.jsonl', captioner,None, './outputs')
    experiment(r'./data/annotations.jsonl',captioner,[FlipImage()],'./outputs')
    experiment(r'./data/annotations.jsonl',captioner,[BlurImage(5)],'./outputs')
    experiment(r'./data/annotations.jsonl',captioner,[RescaleImage(0.5)],'./outputs')
    experiment(r'./data/annotations.jsonl',captioner,[RescaleImage(2)],'./outputs')
    experiment(r'./data/annotations.jsonl',captioner,[RotateImage(270)],'./outputs')
    experiment(r'./data/annotations.jsonl',captioner,[RotateImage(45)],'./outputs') 
    


if __name__ == '__main__':
    main()
