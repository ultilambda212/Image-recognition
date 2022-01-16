import numpy as np
from cv2 import cv2

class Image:
    def readImage(self, filePath):
        # Load image and aply grayscale
        img = cv2.imread(filePath, 0)
        return img

    def readImages(self, imageFile, imageNames):
        images = []
        for imageName in imageNames:
            imagePath = imageFile + '/' + imageName
            image = self.readImage(imagePath)
            images.append(image)
        arrImages = np.array(images)
        return arrImages
