#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("250x200")

#create empty frame (new window for components in root)
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)
#activate grid in said new frame
frame_login.grid(row=0, column=0, sticky="news")
frame_auth.grid(row=0, column=0, sticky="news")

def login():
    frame_auth.tkraise()

#frame login widgets
lbl_username = tk.Label(frame_login, text='Username:', fg='blue', font='Times 15')
lbl_username.pack(padx=50)


#text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()


#both above but for the password
lbl_password = tk.Label(frame_login, text='Password:', fg='blue', font='Times 15')
lbl_password.pack(padx=50)

ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack()

#button for logging in
button_login = tk.Button(frame_login, text='Login', command=login)
button_login.pack(pady=10)

#auth label
lbl_authorized = tk.Label(frame_auth, text='Authorization screen', fg='blue', font='Times 15')
lbl_authorized.pack(padx=50)

frame_login.tkraise()
root.mainloop()