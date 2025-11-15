# import tkinter
#
# root = tkinter.Tk()
#
# entry = tkinter.Entry(root)
# entry.pack()
#
#
# def show_input(event=None):
#     print("Enter was pressed.")
#
# root.bind("<>", show_input())
# root.mainloop()

import tkinter

root = tkinter.tk()
entry_var = tkinter.stringVar(root, value=)
entry = tkinter.Entry(root, textvariable=entry_var)
entry.pack()

label_var = tkinter.StringVar(root, value="")
label = tkinter.label(root, textvariable=label_var)
label.pack()

def show_input(event=None):
    given_text = entry_var.get()
    label_var.set(given_text)
    entry.delete(firs:0 last:"end")