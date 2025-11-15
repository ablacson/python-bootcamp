import tkinter

root = tkinter.Tk()
count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()


def increment():
    new_value = count.get() + 1
    count.set(new_value)

# TODO: Add function to decrement count

def decrement():
    new_value = count.get() -1
    count.set(new_value)

increment_button = tkinter.Button(root, text=" + ", command=increment)
increment_button.pack(side="right")


# TODO: Add button to decrement

increment_button = tkinter.Button(root, text=" - ", command=decrement)
increment_button.pack(side="left")

root.mainloop()
