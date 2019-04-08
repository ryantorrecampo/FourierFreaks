from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from skimage.io import imread
import skimage.transform as skt

#Creates and sets the size of the GUI window
window = Tk()
window.geometry("820x820")
window.title("Filtering in Frequency Domain")

# Creates the text for the buttons/entries
Label(window, text="1. Select an Image", font=("Ariel", 12), fg="blue").grid(row=0)
Label(window, text="2. Select Filter", font=("Ariel", 12), fg="blue").grid(row=0, column=1)
Label(window, text="3. Enter Cutoff", font=("Ariel", 12), fg="blue").grid(row=0, column=2)
Label(window, text="4. Enter Order", font=("Ariel", 12), fg="blue").grid(row=0, column=3)

# Sets the defualts of the program
img = "Image1.png"
filter = "Ideal High Pass"
print("Default image is: " + img)
print("Default filter is: " + filter)

# Changes the image
def iValue(value):
    global img
    img = value+".png"
    print("You have selected " + img)

# Changes the filter
def fValue(value):
    global filter
    filter = value
    print(filter)

def run():
    print("***RUNNING***")
    cutoff = setCutoff.get()
    order = setOrder.get()
    print("Image = ", img)
    print("Filter = ", filter)
    print("Cutoff = ", cutoff)
    print("Order = ", order)

    image = imread(img, as_gray=True)
    msg = "**SOMETHING GOES HERE**"

    a1 = fig.add_subplot(221)
    a1.imshow(image, cmap=plt.cm.Greys_r)
    a1.set_title("Original Image")

    fig.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(row=2, columnspan=5)
    Label(window, text=msg, font=("Ariel", 10), fg="red").grid(row=3, sticky=NE)
    canvas.draw()


iList = ["Image1", "Image2", "Image3", "Image4", "Image5", "Image6"]
filterList = ["Ideal High Pass", "Ideal Low Pass", "Gaussian High Pass", "Gaussian Low Pass", "Butterworth High Pass",
              "Butterworth Low Pass"]

# Image
var1 = StringVar()
var1.set("Image1")
# Filter
var2 = StringVar()
var2.set("Ideal High Pass")
# Cutoff
var3 = StringVar()
var3.set(15)
# Order
var4 = StringVar()
var4.set(2)

# Image menu
setImg = OptionMenu(window, var1, *iList, command=iValue)
setImg.configure(font=("Times"))
setImg.grid(row=1, column=0)
# Filter menu
setFilter = OptionMenu(window, var2, *filterList, command=fValue)
setFilter.configure(font=("Times"))
setFilter.grid(row=1, column=1)
# Cutoff Entry
setCutoff = Entry(window, textvariable=var3)
setCutoff.configure(font=("Times"))
setCutoff.grid(row=1, column=2)
# Order Entry
setOrder = Entry(window, textvariable=var4)
setOrder.configure(font=("Times"))
setOrder.grid(row=1, column=3)


fig = Figure(figsize=(7, 7))
canvas = FigureCanvasTkAgg(fig, master=window)

# RUN button
button1 = Button(window, text="**RUN**", bg="red", font=("Times", 12), command=run)
button1.grid(row=1, column=4, padx=30, pady=15)

window.mainloop()