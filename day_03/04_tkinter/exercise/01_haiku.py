import tkinter

root = tkinter.Tk()

root.title("Python Haiku")
message = """
Loops within loops again
A silent function returns
The logic is clear.
"""

# TODO: Show message using a label
label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()
