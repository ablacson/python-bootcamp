import tkinter

root = tkinter.Tk()

root.title("Feedback Form")


# TODO: Create StringVar for name
# TODO: Create StringVar for name

name_frame = tkinter.Frame(root)
name_frame.pack()

name = tkinter.Label(name_frame, text="Name")
name.pack(side="left")
name_entry_var = tkinter.StringVar()
name_entry = tkinter.Entry(name_frame, textvariable=name_entry_var)
name_entry.pack(side="right")

# TODO: Create StringVar for age
# TODO: Create StringVar for age

age_frame = tkinter.Frame(root)
age_frame.pack()

age = tkinter.Label(age_frame, text="Age")
age.pack(side="left")
age_entry_var = tkinter.IntVar()
age_entry = tkinter.Entry(age_frame, textvariable=age_entry_var)
age_entry.pack(side="right")



# TODO: Create StringVar for theme
# TODO: Create StringVar for theme

# TODO: Create BooleanVar for subscribe
# TODO: Create BooleanVar for subscribe

# TODO: Create IntVar for rating
# TODO: Create IntVar for rating

# TODO: Create function for saving values to JSON
# TODO: Create button for submit + save


def save_data(event=None):
    data ={
        "Name": name_entry_var.get(),
        "Age": age_entry_var.get(),
        "Theme": theme_var.get(),
    }




root.mainloop()
