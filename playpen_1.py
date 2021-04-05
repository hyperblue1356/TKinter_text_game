# Make questions and input box to type answer, answer saved to player info
# Create a function to retrieve data from result box and save to player data.

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import time
import os

mainWindow = tkinter.Tk()
mainWindow.title = "Radiants"
mainWindow.geometry = "640x480"

# Questions

question_list = ["I am the remnants of Honour, What is your name?", "What is your age?",
                 "Choose a race you would like to know more about",
                 "Would you like to know about another race?: ",
                 "What race are you?: ",
                 "Choose an order you would like to know more about: ",
                 "Would you like to know about another order?: ",
                 "What order are you?: ", ]

# For player data i.e name, age etc



# Function to bring up next question in question_list into my_label

def counter():
    global question_list

    my_label.config(text=question_list.pop(0))
    Create_result_box()


# Function to create Entry window for player to input there own data

def Create_result_box():
    start.destroy()
    result = tkinter.Entry(mainWindow)
    result.grid(row=2, column=0, sticky='sw')
    result.get()
    return result



# Widgets

canvas1 = tkinter.Canvas(mainWindow, width=640, height=480)
canvas1.grid(row=0, column=0, rowspan=2, sticky="nsew")

frame1 = tkinter.Frame(canvas1, relief="sunken", borderwidth=1, )
frame1.grid(row=0, column=0, sticky='EW')

my_label = tkinter.Label(frame1, background="White")
my_label.grid(row=0, column=0)

start = tkinter.Button(frame1, text="Start", command=counter)
start.grid(row=1, column=0)

my_button = tkinter.Button(frame1, text="Enter", command=counter)
my_button.grid(row=2, column=1)




# Start the GUI
mainWindow.mainloop()
