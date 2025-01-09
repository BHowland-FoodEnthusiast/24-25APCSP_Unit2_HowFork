#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

#create empty frame (new window for components in root)
frame_login = tk.Frame(root)

#activate grid in said new frame
frame_login.grid()

#frame login widgets
lbl_username = tk.Label(frame_login, text='Username:', fg='blue', font=('Times 200'))
lbl_username.pack(padx=50, pady=50)

#text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)


root.mainloop()