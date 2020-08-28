from tkinter import *
from tkinter import messagebox as mb
window=Tk()
window.title("Stone Paper Scissor")
window.configure(background='blue')
window.minsize(width=350,height=330)
img=PhotoImage(file=r"C:\Users\NITISH GAUR\Pictures\screenshots\paper.png",width=300,height=150)
Button(window,image=img).place(x=10,y=20)
def x():
    if mb.askyesno("Stone Paper Scissor","Do you really want to quit"):
       
        window.destroy()
    else:
        mb.showinfo('cancelled',"you click cancelled")
        
    

        
 
Button(window,text='Quit',bg="red",fg="white",padx=10,bd=15,command=x).place(x=110,y=260)
def y():
    window=Tk()
    window.title("Game")
    window.minsize(width=300,height=300)
    window.configure(background='green')
    b=Label(window,text='Enter name',bg="green",fg="white",font=("gabriola",15))
    b.place(x=10,y=70)
    c=Entry(window)
    c.place(x=90,y=85)
    a=Label(window,text="You vs Computer",bg='green',fg='yellow',font=("gabriola",25))
    a.place(x=35,y=10)
    Button(window,text='OK',bg="yellow",fg="black",pady=1,bd=4).place(x=220,y=80)
    Button(window,text='Stone',bg="red",fg="white",padx=10,bd=10).place(x=110,y=140)
    Button(window,text='Paper',bg="red",fg="white",padx=10,bd=10).place(x=110,y=190)
    Button(window,text='Scissor',bg="red",fg="white",padx=10,bd=10).place(x=110,y=240)
Button(window,text='Play',bg="green",fg="white",padx=10,bd=15,command=y).place(x=110,y=200)


    






window.mainloop()
