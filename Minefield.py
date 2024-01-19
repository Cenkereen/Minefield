import tkinter as tk
import random
from tkinter import messagebox

bomb1=0
bomb2=0
bomb3=0
bomb4=0
bomb5=0
bomb6=0
liste=[]
count=0

for i in range(36):
    liste.append(0)

def bomb():
    global bomb1,bomb2,bomb3,bomb4,bomb5,bomb6
    bomb1=random.randint(0,35)
    bomb2=random.randint(0,35)
    bomb3=random.randint(0,35)
    bomb4=random.randint(0,35)
    bomb5=random.randint(0,35)
    bomb6=random.randint(0,35)
    if bomb1==bomb2 or bomb1==bomb3 or bomb1==bomb4 or bomb1==bomb5 or bomb1==bomb6 or bomb2==bomb3 or bomb2==bomb4 or bomb2==bomb5 or bomb2==bomb6 or bomb3==bomb4 or bomb3==bomb5 or bomb3==bomb6 or bomb4==bomb5 or bomb4==bomb6 or bomb5==bomb6:
        return bomb()

bomb()
liste[bomb1]="X"
liste[bomb2]="X"
liste[bomb3]="X"
liste[bomb4]="X"
liste[bomb5]="X"
liste[bomb6]="X"

def side(n):
    if n>0 and n!=6 and n!=12 and n!=18 and n!=24 and n!=30 and liste[n-1]!="X":
        liste[n-1]+=1
    if n>5 and liste[n-6]!="X":
        liste[n-6]+=1
    if n!=35 and n!=5 and n!=11 and n!=17 and n!=23 and n!=29 and liste[n+1]!="X":
        liste[n+1]+=1
    if n<30 and liste[n+6]!="X":
        liste[n+6]+=1
    if n>5 and n!=11 and n!=17 and n!=23 and n!=29 and n!=35 and liste[n-5]!="X":
        liste[n-5]+=1
    if n>5 and n!=6 and n!=12 and n!=18 and n!=24 and n!=30 and liste[n-7]!="X":
        liste[n-7]+=1
    if n<30 and n!=0 and n!=6 and n!=12 and n!=18 and n!=24 and liste[n+5]!="X":
        liste[n+5]+=1
    if n<29 and n!=5 and n!=11 and n!=17 and n!=23 and liste[n+7]!="X":
        liste[n+7]+=1


side(bomb1)
side(bomb2)
side(bomb3)
side(bomb4)
side(bomb5)
side(bomb6)

def click(n,m):
    global count
    n["text"]=liste[m]
    if n["text"]=="X":
        n["bg"]="red"
        count += 1
    check(n)

def check(n):
    if n["text"]=="X" or count==30:
        response = messagebox.askyesno("Mayın Tarlası", "Tekrar?")
        if response:
            reset()
        else:
            form.quit()

form = tk.Tk()
form.title("Mayın Tarlası")
form.geometry("510x510+700+250")


def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,count
    count=0
    b1 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b1,0))
    b1.grid(row=0, column=0)
    b2 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b2,1))
    b2.grid(row=0, column=1)
    b3 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b3,2))
    b3.grid(row=0, column=2)
    b4 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b4,3))
    b4.grid(row=0, column=3)
    b5 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b5,4))
    b5.grid(row=0, column=4)
    b6 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b6,5))
    b6.grid(row=0, column=5)
    b7 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b7,6))
    b7.grid(row=1, column=0)
    b8 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b8,7))
    b8.grid(row=1, column=1)
    b9 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b9,8))
    b9.grid(row=1, column=2)
    b10 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b10,9))
    b10.grid(row=1, column=3)
    b11 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b11,10))
    b11.grid(row=1, column=4)
    b12 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b12,11))
    b12.grid(row=1, column=5)
    b13 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b13,12))
    b13.grid(row=2, column=0)
    b14 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b14,13))
    b14.grid(row=2, column=1)
    b15 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b15,14))
    b15.grid(row=2, column=2)
    b16 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b16,15))
    b16.grid(row=2, column=3)
    b17 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b17,16))
    b17.grid(row=2, column=4)
    b18 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b18,17))
    b18.grid(row=2, column=5)
    b19 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b19,18))
    b19.grid(row=3, column=0)
    b20 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b20,19))
    b20.grid(row=3, column=1)
    b21 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b21,20))
    b21.grid(row=3, column=2)
    b22 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b22,21))
    b22.grid(row=3, column=3)
    b23 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b23,22))
    b23.grid(row=3, column=4)
    b24 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b24,23))
    b24.grid(row=3, column=5)
    b25 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b25,24))
    b25.grid(row=4, column=0)
    b26 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b26,25))
    b26.grid(row=4, column=1)
    b27 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b27,26))
    b27.grid(row=4, column=2)
    b28 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b28,27))
    b28.grid(row=4, column=3)
    b29 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b29,28))
    b29.grid(row=4, column=4)
    b30 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b30,29))
    b30.grid(row=4, column=5)
    b31 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b31,30))
    b31.grid(row=5, column=0)
    b32 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b32,31))
    b32.grid(row=5, column=1)
    b33 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b33,32))
    b33.grid(row=5, column=2)
    b34 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b34,33))
    b34.grid(row=5, column=3)
    b35 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b35,34))
    b35.grid(row=5, column=4)
    b36 = tk.Button(form, text=" ", font="Times 20", bg="white", height=2, width=5,command=lambda: click(b36,35))
    b36.grid(row=5, column=5)

reset()

form.mainloop()
