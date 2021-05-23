# Some questions don't make sense without more context or some questions don't need the answer displayed i.e "Do you want to know more?"
# Consider integrating other parts of text_game_main such as the classes etc. Do this by putting them in a function the nassigning to tkinter
# Input box need to be destroyed and rebuilt after each question.
# Make UI look better


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

player_info = []

def counter():
    global question_list
    global player_info

    my_label.config(text=question_list.pop(0))
    destroy_start()

    player_info1.config(text=player_info)

    answer = result.get()
    player_info.append(answer)
    if "cool" in my_label:
        print("Let's move on")










# Function to destroy start button
def destroy_start():
    start.destroy()



# Widgets

canvas1 = tkinter.Canvas(mainWindow, width=640, height=480)
canvas1.grid(row=0, column=0, rowspan=2, sticky="nsew")

frame1 = tkinter.Frame(canvas1, relief="sunken", borderwidth=1, )
frame1.grid(row=0, column=0, sticky='EW')

my_label = tkinter.Label(frame1, background="White")
my_label.grid(row=0, column=0)

player_info1 = tkinter.Label(frame1, background="white")
player_info1.grid(row=3, column=3)

start = tkinter.Button(frame1, text="Start", command=counter)
start.grid(row=1, column=0)

enter_button = tkinter.Button(frame1, text="Enter", command=counter)
enter_button.grid(row=2, column=1)

result = tkinter.Entry(mainWindow)
result.grid(row=2, column=0, sticky='sw')




# Start the GUI
mainWindow.mainloop()
