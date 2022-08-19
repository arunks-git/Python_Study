from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox

def exiting():
    exit()


def abt():
    tkinter.messagebox.showinfo("About" , "This is registration form developed in Python 3.8")

window = Tk()
window.geometry("800x700")
window.configure(background='white')
window.title("Registration Form")

img = Image.open("/Users/arunks/Downloads/regicon.jpeg")
photo=ImageTk.PhotoImage(img)

plabel=Label(image=photo).place(x=500 , y=100)

menubar = Menu(window)
window.configure(menu=menubar)

subm1=Menu(menubar)
menubar.add_cascade(label="File",menu=subm1)
subm1.add_command(label="Exit",command=exiting)

subm2=Menu(menubar)
menubar.add_cascade(label="Option",menu=subm2)
subm2.add_command(label="About" , command=abt)


fn = StringVar()
ln = StringVar()
db = StringVar()
var_c1 = StringVar()
var_r1 = StringVar()

def second_win():
    window1 = Tk()
    window1.geometry("300x100")
    window1.title("Help")
    label21 = Label(window1, text="Contact admin@admin", relief="solid", width=20, font=('arial', 12, "bold")).place(x=50,y=20)
    button21 = Button(window1, text="Close", width=12, bg='brown', fg='white', command=window1.destroy).place(x=180 , y = 100)


def printing():

    print(f'Name is {fn.get()} {ln.get()} and you are from {cn.get()}')
    print(f'You are {var_r1.get()} and knows {var_c1.get()}')
    tkinter.messagebox.showinfo("Info" , f"User {fn.get()} {ln.get()} is registered")



label1 = Label(window,text="Registration Form" , relief = "solid" , width=20,font=('arial',19,"bold"))
label1.place(x=90,y = 50)
label2 = Label(window,text="FirstName :" , width=20,font=('arial',10,"bold"))
label2.place(x=80,y = 130)

entry1=Entry(window,textvar=fn).place(x=200,y=130)

label20 = Label(window,text="LastName :" , width=20,font=('arial',10,"bold"))
label20.place(x=80,y = 200)

entry2=Entry(window,textvar=ln).place(x=200,y=200)

label3 = Label(window,text="DOB :" , width=20,font=('arial',10,"bold"))
label3.place(x=80,y = 280)

entry3=Entry(window,textvar=db).place(x=200,y=280)

label4 = Label(window,text="Country" , width=20,font=('arial',10,"bold"))
label4.place(x=80,y = 370)

cn = StringVar()
list1 = ['India' , 'US' , 'UK']
droplist = OptionMenu(window,cn,*list1)
cn.set("Select Country")
droplist.config(width=15)
droplist.place(x=200,y=370)

label5 = Label(window,text="Lang : " , width=20,font=('arial',10,"bold"))
label5.place(x=80,y = 420)

c1=Checkbutton(window,text='Java',variable=var_c1 , onvalue='Java').place(x=235 , y=420)
c2=Checkbutton(window,text='Python',variable=var_c1 , onvalue='Python').place(x=290 , y=420)

label6 = Label(window,text="Gender :" , width=20,font=('arial',10,"bold"))
label6.place(x=80,y = 459)

r1=Radiobutton(window,text='Male',variable=var_r1,value='Male').place(x=230 , y=460)
r2=Radiobutton(window,text='Female',variable=var_r1,value='Female').place(x=290 , y=460)

button1 = Button(window,text="Signup", width=12 , bg='brown', fg='white' , command=printing)
button1.place(x=150,y=500)
button2 = Button(window,text="Quit", width=12 , bg='brown', fg='white' , command=exiting)
button2.place(x=280,y=500)
button3 = Button(window,text="Help", width=12 , bg='brown', fg='white' , command=second_win)
button3.place(x=200,y=550)

window.mainloop()


'''
label1 = Label(window,text="Welcome here" ,fg='yellow',bg='black', relief='solid',font=('arial',15,"bold")).pack()
#label2 = Label(window,text="Welcome here again")
#label2.pack(fill=BOTH,padx=1,pady=1,expand=True)
label3 = Label(window,text="You there" ,fg='yellow',bg='black', relief='solid',font=('arial',15,"bold")).place(x=1,y=20)

button1 = Button(window,text="Click")
button1.place(x=1,y=60)

window.mainloop()
'''