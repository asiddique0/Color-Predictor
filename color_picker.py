from tkinter import *
import numpy as np 
import pandas as pd 
import random as rd 
from keras.models import load_model
from sklearn.externals import joblib
import warnings
warnings.filterwarnings("ignore")

# save the path(s)
NN_path = r"C:\\Users\\user\\Desktop\\Jupyter Projects\\color_project\\color_classifier_NN.h5"
SVM_path = r"C:\\Users\\user\\Desktop\\Jupyter Projects\\color_project\\color_classifier_svm.pkl"
scaler_path = r"C:\\Users\\user\\Desktop\\Jupyter Projects\\color_project\\Standard_Scaler.pkl"
# load the classifiers
NN_clf = load_model(NN_path)
SVM_clf = joblib.load(SVM_path)
scaler = joblib.load(scaler_path)

# get a color scheme
def colorOne():
	return rd.randint(1, 255)

def colorTwo():
	return rd.randint(1, 255)

def colorThree():
	return rd.randint(1, 255)

def getColor():
	x, y, z = (colorOne(), colorTwo(), colorThree())
	array = scaler(np.array([x, y, z]).reshape(-1,1))
	array = np.array(array).reshape(1,-1)
	return ('#%02x%02x%02x' % (x, y, z)), array

# Begin main
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

background, colors = getColor()

top_1 = Label(root, text="The Quick Brown Fox Jumps\t", fg="white", bg=background, font=("Arial", 20))
top_2 = Label(root, text="The Quick Brown Fox Jumps\t", fg="black", bg=background, font=("Arial", 20))

# event if the user selects white
def click_white():
	background, x = getColor()
	top_1.configure(background=background)
	top_2.configure(background=background)
	svm_prediction = int(SVM_clf.predict(x))
	nn_prediction = NN_clf.predict(x)
	nn_prediction = int(nn_prediction>0.5)
	message = ("SVM: %d NN: %d" %(svm_prediction, nn_prediction))
	info_label.configure(text=message)
# event if the user selects black
def click_black():
	background, x = getColor()
	top_1.configure(background=background)
	top_2.configure(background=background)
	svm_prediction = SVM_clf.predict(x)
	nn_prediction = NN_clf.predict(x)
	nn_prediction = int(nn_prediction>0.5)
	message = ("SVM: %d NN: %d" %(svm_prediction, nn_prediction))
	info_label.configure(text=message)

# defining the layout
info_label = Label(bottomFrame, text="Click to see predictions!", font=("Arial", 10))
bottom_1 = Button(bottomFrame, text="White", font=("Arial", 14), command=click_white)
bottom_2 = Button(bottomFrame, text="Black", font=("Arial", 14), command=click_black)

top_1.pack(side=LEFT, fill=BOTH, expand=1)
top_2.pack(side=LEFT, fill=BOTH, expand=1)

bottom_1.pack(side=LEFT, fill=BOTH, expand=1)
bottom_2.pack(side=LEFT, fill=BOTH, expand=1)
info_label.pack(side=RIGHT, fill=BOTH, expand=1)

root.mainloop()
# End main