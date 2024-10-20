from tkinter import *
from tkinter import messagebox

w = Tk()
w.configure(bg = "black")
w.geometry("700x700")
w.title("tic tac toe game")

tog = True
r = 0
def click(but):
    global tog, r
    if(but["text"]=="" and tog == True):
        but["text"]="X"
        tog=False
        r=r+1
    elif(but["text"]=="" and tog == False):
        but["text"]="O"
        tog=True
        r=r+1
    if(b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or
       b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or
       b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X" or
       b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or
       b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or
       b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X" or
       b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or
       b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X"):
        r=0
        print("X won")
        messagebox.showinfo("Result", "X Won")

    elif(b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or
       b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or
       b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O" or
       b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or
       b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or
       b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O" or
       b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or
       b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O"):
        r=0
        print("O won")
        messagebox.showinfo("Result", "O Won")
       

f1 = Frame(w)
f1.pack()
b1 = Button(f1, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b1))
b1.pack(side = LEFT)
b2 = Button(f1, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b2))
b2.pack(side = LEFT)
b3 = Button(f1, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b3))
b3.pack(side = LEFT)

f2 = Frame(w)
f2.pack()
b4 = Button(f2, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b4))
b4.pack(side = LEFT)
b5 = Button(f2, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b5))
b5.pack(side = LEFT)
b6 = Button(f2, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b6))
b6.pack(side = LEFT)

f3 = Frame(w)
f3.pack()
b7 = Button(f3, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b7))
b7.pack(side = LEFT)
b8 = Button(f3, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b8))
b8.pack(side = LEFT)
b9 = Button(f3, text = "",font = ("arial",20,"bold"), width=12, height = 5,command = lambda:click(b9))
b9.pack(side = LEFT)

w.mainloop()
