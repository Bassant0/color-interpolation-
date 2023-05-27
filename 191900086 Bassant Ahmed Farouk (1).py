import tkinter
from tkinter import *
from tkinter import colorchooser
import tkinter as tk

import tkinter as tk

color1=[]
color2=[]
color3=[]
color4=[]
window = tk.Tk()
window.title('Bilinear interpolation')
label = tk.Label(window, text="Please choose 4 colors:", font=("Verdana", 15, "bold"), fg="blue")


def b1_pressed():
    # code to be executed when the button is clicked
    color = tkinter.colorchooser.askcolor()
    b1.config(bg=color[1])
    # extract the RGB values from the color tuple
    r, g, b = color[0]
    color1.append(r)
    color1.append(g)
    color1.append(b)

def b2_pressed():
    # code to be executed when the button is clicked
    color = tkinter.colorchooser.askcolor()
    b2.config(bg=color[1])
    # extract the RGB values from the color tuple
    r, g, b = color[0]

    color2.append(r)
    color2.append(g)
    color2.append(b)


def b3_pressed():
    # code to be executed when the button is clicked
    color = tkinter.colorchooser.askcolor()
    b3.config(bg=color[1])
    # extract the RGB values from the color tuple
    r, g, b = color[0]
    color3.append(r)
    color3.append(g)
    color3.append(b)


def b4_pressed():
    # code to be executed when the button is clicked
    color = tkinter.colorchooser.askcolor()
    b4.config(bg=color[1])
    # extract the RGB values from the color tuple
    r, g, b = color[0]

    color4.append(r)
    color4.append(g)
    color4.append(b)

def b5_pressed():
    rgb = []
    col1 = [color1[0] * (1 - 0.57) + color2[0] * 0.57,
          color1[1] * (1 - 0.57) + color2[1] * 0.57,
          color1[2] * (1 - 0.57) + color2[2] * 0.57]
    col2 = [color3[0] * (1 - 0.57) + color4[0] * 0.57,
          color3[1] * (1 - 0.57) + color4[1] * 0.57,
          color3[2] * (1 - 0.57) + color4[2] * 0.57]

    # Interpolate the colors in the y direction
    interpolation = [col1 [0] * (1 - 0.5) + col2[0] *0.5,
    col1 [1] * (1 - 0.5) + col2[1] * 0.5,
    col1 [2] * (1 - 0.5) + col2[2] * 0.5]

    rgb.append(int (interpolation[0]))
    rgb.append(int (interpolation[1]))
    rgb.append(int(interpolation[2]))

    ctuple = tuple(rgb)
    ctuple= "#%02x%02x%02x" % ctuple
    b5.config(bg=ctuple)

    #  button is pressed then

    red_entry.delete(0, 'end')
    red_entry.insert(0, str(rgb[0]))
    green_entry.delete(0, 'end')
    green_entry.insert(0, str(rgb[1]))
    blue_entry.delete(0, 'end')
    blue_entry.insert(0, str(rgb[2]))



def add_border(event):
    event.widget.config(bd=5)

def remove_border(event):
    event.widget.config(bd=1)



b1 = tk.Button(window, text="Color 1", command=b1_pressed, bg="lightgray", width=30, height=10)
b1.bind( "<Enter>", add_border)
b1.bind( "<Leave>", remove_border)
b2 = tk.Button(window, text="Color 2", command=b2_pressed, bg="lightgray", width=30, height=10)
b2.bind( "<Enter>", add_border)
b2.bind( "<Leave>", remove_border)
b3 = tk.Button(window, text="Color 3", command=b3_pressed, bg="lightgray", width=30, height=10)
b3.bind( "<Enter>", add_border)
b3.bind( "<Leave>", remove_border)
b4 = tk.Button(window, text="Color 4", command=b4_pressed, bg="lightgray", width=30, height=10)
b4.bind( "<Enter>", add_border)
b4.bind( "<Leave>", remove_border)

b1.grid(row=1, column=0)
b2.grid(row=1, column=2)
b3.grid(row=3, column=0)
b4.grid(row=3, column=2)


red_entry = tk.Entry(window, width=20)
red_entry.insert(0, "0")
red_entry.grid(row = 5, column = 0, pady=10)

green_entry = tk.Entry(window, width=20)
green_entry.insert(0, "0")
green_entry.grid(row = 5, column = 1, pady=10)

blue_entry = tk.Entry(window, width=2)
blue_entry.insert(0, "0")
blue_entry.grid(row = 5, column = 2, pady=10)


b5 = tk.Button(window, text="Expected color", command=b5_pressed,width=30, height=10)
b5.bind( "<Enter>", add_border)
b5.bind( "<Leave>", remove_border)
b5.grid(row=2, column=1)

# start the event loop

label.grid(row = 0, column = 1, pady=10)


window.mainloop()
