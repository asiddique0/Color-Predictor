from tkinter import *
import numpy as np 
import pandas as pd 
import random as rd 
# training labels
labels = []
# accompanying data
color_1 = []
color_2 = []
color_3 = []
# get the color values and append them to their respective arrays
def colorOne():
	x = rd.randint(1, 255)
	global color_1
	color_1 = np.append(color_1, x)
	return x

def colorTwo():
	x = rd.randint(1, 255)
	global color_2
	color_2 = np.append(color_2, x)
	return x

def colorThree():
	x = rd.randint(1, 255)
	global color_3
	color_3 = np.append(color_3, x)
	return x

def getColor():
	return '#%02x%02x%02x' % (colorOne(), colorTwo(), colorThree())
# begin main
root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

background = getColor()

top_1 = Label(root, text="The Quick Brown Fox Jumps\t", fg="white", bg=background, font=("Arial", 20))
top_2 = Label(root, text="The Quick Brown Fox Jumps\t", fg="black", bg=background, font=("Arial", 20))
# save the users choice for white
def click_white():
	global labels
	labels = np.append(labels, 1)
	background = getColor()
	top_1.configure(background=background)
	top_2.configure(background=background)
# save the users choice for black
def click_black():
	global labels
	labels = np.append(labels, 0)
	background = getColor()
	top_1.configure(background=background)
	top_2.configure(background=background)
# defining layout
bottom_1 = Button(bottomFrame, text="White", font=("Arial", 14), command=click_white)
bottom_2 = Button(bottomFrame, text="Black", font=("Arial", 14), command=click_black)

top_1.pack(side=LEFT, fill=BOTH, expand=1)
top_2.pack(side=LEFT, fill=BOTH, expand=1)

bottom_1.pack(side=LEFT, fill=BOTH, expand=1)
bottom_2.pack(side=LEFT, fill=BOTH, expand=1)

root.mainloop()
# End main

# defining a np.array object instead of using a reg list
labels = np.insert(labels, 0, np.NaN, axis=0)
labels = np.array(labels).transpose()
color_1 = np.array(color_1).transpose()
color_2 = np.array(color_2).transpose()
color_3 = np.array(color_3).transpose()

# making sure the dimensions match
print(labels.shape, color_1.shape, color_2.shape, color_3.shape)

# defining a dataFrame object so we can save the output
df = pd.DataFrame(np.array([labels, color_1, color_2, color_3]))
df = df.T
# renaming columns
df = df.rename(columns={0:"labels", 1:"color_1", 2:"color_2", 3:"color_3"})
df.labels = df.labels.shift(-1)

# saving them to a csv file for processing
# pd.DataFrame(df).to_csv(r"C:\\Users\\user\\Desktop\\data_collection\\collect_color_data.csv"))
