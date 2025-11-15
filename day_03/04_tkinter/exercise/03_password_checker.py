import tkinter

root = tkinter.Tk()

# TODO: Add label for instructions
# TODO: Add entry for instructions
# TODO: Add StringVar for instruction
# TODO: Add label using StringVar

root.title("Password Checker")

text = tkinter.StringVar(root, value="Enter your password.")
label = tkinter.Label(root, textvariable = text)
label.pack()

entry = tkinter.Entry(root)
entry.pack()

text2 = tkinter.StringVar(root, value="Enter your password and press Enter.")
label2 = tkinter.Label(root, textvariable = text2)
label2.pack()

def check_password(event=None):
    correct_password = "pass"
    if correct_password == entry.get():
        text2.set("Correct")
    else:
        text2.set("Incorrect")


    # TODO: Check if entry.get() has correct value


# TODO: Add key bindings for check_password
button = tkinter.Button(root, text="Submit", command=check_password)
button.pack()
root.bind("<Return>",check_password)
root.mainloop()
