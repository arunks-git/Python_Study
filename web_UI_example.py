import tkinter as tk
from tkinter import ttk

def hello():
    print(f"Hello , {username.get() or 'World'}")

root = tk.Tk()
root.title("Hello")
username = tk.StringVar()

name_label = ttk.Label(root , text='Name: ')
name_label.pack(side='left' , padx=(0,10))
name_entry = ttk.Entry(root , width=15 , textvariable=username)
name_entry.pack(side='left')
name_entry.focus()

hello_button = ttk.Button(root , text='Click for message' , command=hello)
hello_button.pack(side='bottom' , fill='x' , expand=True)
quit_button = ttk.Button(root , text='Click to Quit' , command=root.destroy)
quit_button.pack(side='bottom' , fill='x' , expand=True)

root.mainloop()
