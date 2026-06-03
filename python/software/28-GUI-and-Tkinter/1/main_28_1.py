"""

GUI (GRAPHICAL USER INTERFACE) WITH TKINTER MODULE:
http://tcl.tk/man/tcl8.7/TkCmd/entry.html

To install TKinter through terminal, use:
    >> pip install tk

"""

from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("My fist GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 12, "bold"))  # creating a label text
my_label.pack()  # 'pack()' method set the new component on screen


# Button
def button_clicked():
    new_text = input_1.get()
    my_label.config(text=new_text)  # changing a pre-created label text.


button = Button(text="Click Me", command=button_clicked)  # button creation
button.pack()  # 'pack()' method set the new component on screen

# Field/Data entry:
input_1 = Entry(width=10)
input_1.pack()  # 'pack()' method set the new component on screen

window.mainloop()  # keep the Tkinter window on screen
