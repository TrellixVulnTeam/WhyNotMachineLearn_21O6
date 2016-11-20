#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#These twolinesreducethetrainingsetsdownto 1%of their originals.
features_train=features_train[:len(features_train)/100]
labels_train=labels_train[:len(labels_train)/100]

from sklearn.svm import SVC
clf = SVC(kernel="linear")
t0 =time()
#fit the data
print ('fitting data now')
clf.fit(features_train, labels_train)
print "trainingtime: ", round(time()-t0,3),"s"
#let it make a prediction
t0= time()
prediction = clf.predict(features_test)
print "trainingtime: ", round(time()-t0,3),"s"
print('checking accuracy')
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(prediction, labels_test)

print(accuracy)
