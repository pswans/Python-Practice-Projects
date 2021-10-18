#inspired by https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/

from tkinter import *
from tkinter import font
from tkinter.ttk import *

from time import strftime as sysTime

#implicitly creates an instance of Tk interpreter.
#window can now be defined, named--still playing with this.
root = Tk()
root.title('System Clock')

#defines time in the root window; you can adjust different aspects thru sysTime(I believe?)
def time():
    string = sysTime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

#'lbl' is being defined; label now can be defined in different aspects.
#background and foreground are defined; although there are a couple more methods you can define.
lbl = Label(root, font = ('arial', 60, 'bold'), 
    background = '#1f572e',
    foreground = '#9676c2')

#'anchor' states where the label will be packed. 
lbl.pack(anchor = 'center')
time()

mainloop()