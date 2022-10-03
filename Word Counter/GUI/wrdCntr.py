"""
Created By Anandu S Nambiar

Title : Creating a word counter using Python (GUI) (tkinter)

The process is done through,
    1. type Document path int he text box
    2. call fileOp() function to count the words in the document while passing the path
    3. if the document exists the word count is shown
    4. else 'Incorrect Document Path' is shown
"""


import tkinter as tk
import fileOp as fP

frame = tk.Tk()
frame.title("Document Word Counter")
frame.geometry('500x100') #size of window


def msg():
    f1 = inputtxt.get(1.0,"end-1c")
    f = fP.fileOp(f1)
    if f==-1:
        lbl.config(text="Incorrect Document Path")
    else:
         
        txt2="Number of Words in the document are: " + str(f)
        lbl.config(text=txt2)
        
# Textview of 'Enter Document Path'
det = tk.Label(frame,text="Enter Document Path: ")
det.pack()

#Text box
inputtxt = tk.Text(frame,height=1,width=50)
inputtxt.pack()

#button 'Count'
printBtn = tk.Button(frame,text="Count",command=msg)
printBtn.pack()

#show count of document
lbl = tk.Label(frame, text="")
lbl.pack()

frame.mainloop()
