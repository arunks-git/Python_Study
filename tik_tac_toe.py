from tkinter import *
from tkinter import messagebox
#from tkmacosx import Button

window = Tk()
window.title("Tic-Tac-Toe")
#window.geometry("300x300")

clicked = True
count = 0



def disable_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count =+1
        win()

    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count =+1
        win()

    else:
        messagebox.showerror("Tic Tac Toe" , "Already selected")

def win():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg='red')
        b2.config(bg='red')
        b3.config(bg='red')
        winner = True
        messagebox.showinfo("Tic Tac Toe" , "X wins...")
        disable_button()

    elif  b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg='red')
        b5.config(bg='red')
        b6.config(bg='red')
        winner = True
        messagebox.showinfo("Tic Tac Toe" , "X wins...")
        disable_button()

def buttons():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count
    clicked = True
    count = 0
    b1 = Button(window, text = " " , height=3 , width=6 , highlightbackground='yellow', foreground ='blue', command=lambda: b_click(b1))
    b2 = Button(window, text = " " , height=3 , width=6 , foreground='green', background='black', command=lambda: b_click(b2))
    b3 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b3))

    b4 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b4))
    b5 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b5))
    b6 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b6))

    b7 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b7))
    b8 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b8))
    b9 = Button(window, text = " " , height=3 , width=6 , bg="SystemButtonFace" , command=lambda: b_click(b9))

    b1.grid(row=1 , column=1)
    b2.grid(row=1 , column=2)
    b3.grid(row=1 , column=3)
    b4.grid(row=2 , column=1)
    b5.grid(row=2 , column=2)
    b6.grid(row=2 , column=3)
    b7.grid(row=3 , column=1)
    b8.grid(row=3 , column=2)
    b9.grid(row=3 , column=3)

menubar = Menu(window)
window.configure(menu=menubar)

subm1=Menu(menubar)
menubar.add_cascade(label="Options",menu=subm1)
subm1.add_command(label="Reset" , command=buttons)

buttons()

window.mainloop()