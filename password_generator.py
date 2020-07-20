from random import randint

PasswordLength = 25

Password = ""


import tkinter as tk

def UpdateTk():
    password_textbox.delete(0, "end")
    password_textbox.insert(0, Password)

def GeneratePassword():
    global Password
    Password = ""
    PasswordLength = int(PLength.get())
    if PasswordLength > 9999:
        password_textbox.delete(0, "end")
        password_textbox.insert(0, "Please enter a value below 10,000")
        return
    elif PasswordLength < 0:
        password_textbox.delete(0, "end")
        password_textbox.insert(0, "Please enter a value above 0")
        return
    for i in range(PasswordLength):
        Password = Password + chr(randint(32, 125)) # ASCII Characters Range
    UpdateTk()

root = tk.Tk()
root.geometry("400x65")
root.title("Password Generator")
root.resizable(False,False)

PLength = tk.Entry(root,width=4, justify="center")
PLength.pack()
PLength.insert(0, 25)

generate_button = tk.Button(root,width=400)
generate_button["text"] = "Generate Random Password"
generate_button["command"] = lambda: GeneratePassword()
generate_button.pack(side="top")

password_textbox = tk.Entry(root,width=400)
password_textbox.pack()
password_textbox.insert(0, Password)
password_textbox.bind("<Key>", lambda a: "break")
password_textbox.pack()

root.mainloop()
