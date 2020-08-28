from tkinter import *
from tkinter import messagebox as mb

import random


window=Tk()
window.title("Stone Paper Scissor")
window.configure(background='blue')
window.minsize(width=350,height=330)

photo=PhotoImage(file="D:\Python Programs\gm.png")
window.iconphoto(False,photo)


img=PhotoImage(file=r"D:\Python Programs\paper.png",width=300,height=150)
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
    window.configure(background='maroon')


    
    b=Label(window,text='Enter name',bg="maroon",fg="yellow",font=("gabriola",15))
    b.place(x=10,y=70)
    t=Entry(window)
    t.place(x=90,y=85)
    a=Label(window,text="You vs Computer",bg='maroon',fg='white',font=("gabriola",30))
    a.place(x=35,y=10)
    global g


    def get():
        global g
        g=t.get()
        t.delete(0,END)


    def stone():
        p="stone"
        c=None
        com=random.randrange(1,4)
        if com==1:
            c="stone"
            x=(p,"vs",c)
            mb.showinfo(x,"It's a Tie")
        if com==2:
            c="paper"
            x=(p,"vs",c)
            mb.showinfo(x,"Com Wins")
        if com==3:
            c="scissor"
            x=(p,"vs",c)
            z=(g,"Wins")
            mb.showinfo(x,z)
        window.destroy()


    def paper():
        p="paper"
        c=None
        com=random.randrange(1,4)
        if com==1:
            c="stone"
            x=(p,"vs",c)
            z=(g,"Wins")
            mb.showinfo(x,z)
        if com==2:
            c="paper"
            x=(p,"vs",c)
            mb.showinfo(x,"It's a Tie")
        if com==3:
            c="scissor"
            x=(p,"vs",c)
            mb.showinfo(x,"Com Wins")
        window.destroy()



    def scissor():
        p="scissor"
        c=None
        com=random.randrange(1,4)
        if com==1:
            c="stone"
            x=(p,"vs",c)
            mb.showinfo(x,"Com Wins")
        if com==2:
            c="paper"
            x=(p,"vs",c)
            z=(g,"Wins")
            mb.showinfo(x,z)
        if com==3:
            c="scissor"
            x=(p,"vs",c)
            mb.showinfo(x,"It's a Tie")
        window.destroy()
         

    
    Button(window,text='OK',bg="yellow",fg="black",pady=1,bd=4,command=get).place(x=220,y=80)
    
    Button(window,text='Stone',bg="red",fg="white",padx=10,bd=10,command=stone).place(x=110,y=140)
    Button(window,text='Paper',bg="red",fg="white",padx=10,bd=10,command=paper).place(x=110,y=190)
    Button(window,text='Scissor',bg="red",fg="white",padx=10,bd=10,command=scissor).place(x=110,y=240)



Button(window,text='Play',bg="green",fg="white",padx=10,bd=15,command=y).place(x=110,y=200)


    






window.mainloop()
