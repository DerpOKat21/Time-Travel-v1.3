import tkinter as tk
import tkcalendar as Calendar
from tkinter import *
from tkcalendar import Calendar
from PIL import Image, ImageTk

root = Tk()
root.title("Time Travel v1.3")
root.geometry("1014x753")
root.resizable(False, False)

img = Image.open(r"bush.jpeg")
tk_img = ImageTk.PhotoImage(img)

label = Label(root, image=tk_img)
label.pack()

cal = Calendar(root, selectmode="day", date_pattern="mm-dd-yyyy")
cal.place(x = 10, y = 350, width = 338, height = 250)

cal.lift()

text_widget = tk.Text(root)
text_widget.place(x = 5, y = 325, width = 1005, height = 419)

text_widget.insert(tk.END, "Settings")

text_widget.lower()

root.mainloop()