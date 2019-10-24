from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Sample Python GUI")
window.geometry('600x400')
firstLbl = Label(window, text="Click the button")
firstLbl.grid(column=0, row=0)

def firstBtnClicked():
    #secondLbl.configure(text="Output from your python stuff!")
    txtbox.insert(INSERT, "Output from your python stuff goes here! \n")

firstBtn = Button(window, text="Press here!", command=firstBtnClicked)
firstBtn.grid(column=1, row=0)
#secondLbl = Label(window, text="Output goes here")
#secondLbl.grid(column=0, row=1, columnspan=2)

# Fancy Frame
textFrame = LabelFrame(window, text="Output from Python stuff", padx=5, pady=5)
textFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=E+W+N+S)

window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

textFrame.rowconfigure(0, weight=1)
textFrame.columnconfigure(0, weight=1)

# Create the textbox for printing output
txtbox = scrolledtext.ScrolledText(textFrame, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=E+W+N+S)

window.mainloop()
