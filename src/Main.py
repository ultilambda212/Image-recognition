from Text import *
from Image import Image
import numpy as np
import cv2
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import NearestCentroid

import time
timer1 = time.perf_counter()

textHelper = TextClass()
imageHelper = Image()

print('Reading train images and labels...')
trainPaths, trainLabels = textHelper.readText('train.txt')
trainImages = imageHelper.readImages('train', trainPaths)
print('Finished reading training images.')


print('Reading validation images...')
validationPaths, validationLabels = textHelper.readText('validation.txt')
validationImages = imageHelper.readImages('validation', validationPaths)
print('Finished reading validation images.')
print(validationImages)

'''
print('Reading test images...')
testPaths = textHelper.readTestText('test.txt')
testImages = imageHelper.readImages('test', testPaths)
print('Finished reading test images.')
'''

print('Scaling images...')
sc = StandardScaler()

nsamples, nx, ny = trainImages.shape
d2TrainImages = trainImages.reshape((nsamples,nx*ny))
trainImages = sc.fit_transform(d2TrainImages)


nsamples, nx, ny = validationImages.shape
d2ValidationImages = validationImages.reshape((nsamples,nx*ny))
validationImages = sc.transform(d2ValidationImages)
print('Finished scaling images.')


'''
nsamples, nx, ny = testImages.shape
d2TestImages = testImages.reshape((nsamples,nx*ny))
testImages = sc.transform(d2TestImages)
print('Finished scaling images.')
'''


# SVM:
print('Training...')
svm1 = svm.SVC(kernel = 'rbf', C = 54, gamma = 0.0005)
# svm1 = svm.SVC(kernel = 'linear', C = 87)
svm1.fit(trainImages, trainLabels)
print('Finished training.')

print('Predicting...')
predictedLabels = svm1.predict(validationImages)
print('Finished predicting test images.')


'''
# Nearest Centroid:
clf = NearestCentroid()
clf.fit(trainImages, trainLabels)
predictedLabels = clf.predict(validationImages)
'''


'''
print('Predicting...')
predictedLabels = svm1.predict(testImages)
print('Finished predicting test images.')
'''

print('Computing f1_score...')
score = f1_score(validationLabels, predictedLabels, average='macro')
print('f1_score: ', score)

print('Computing confusion matrix...')
confusionMatrix = confusion_matrix(validationLabels, predictedLabels)
print('Confusion matrix:')
print(confusionMatrix)


print('Writing text...')
textHelper.writeText('prezicere.csv', validationPaths, predictedLabels)
print('Finished.')

timer2 = time.perf_counter()
print('The program lasted for  ', "{:.2f}".format((timer2 - timer1) / 60), ' minutes.')
