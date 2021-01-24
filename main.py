from tkinter import *
from tkinter.ttk import *

from time import strftime

clock = Tk()
clock.title("Welcome! I'm Learning")
clock.geometry("800x300")

bg = PhotoImage(file = "NASA.png")

def time() :
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label.after(1000, time)

bg = PhotoImage(file = "NASA.png")
my_label = Label(clock, image = bg) 


my_label.place(x=0, y=0, relwidth = 1, relheight =1)

label = Label(clock, font = ("DS-Digital",100), background = "black", foreground = "white")
label.pack(anchor = 'center', pady=90)
time()

clock.mainloop()




#I'm Currently Trying to make it with canvas
'''
my_canvas = Canvas(clock, width=800, height=300)
my_canvas.pack(fill ="both", expand=True)

#Set Image in Canvas
my_canvas.create_image(0,0,image = bg, anchor="nw")

#Adding Label
my_canvas.create_text(400,250, text = time(), font = ("DS-Digital",100), fill="white")
'''