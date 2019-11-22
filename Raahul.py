from tkinter import*
import os
import csv
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np



rows=[]
des=[]
up=[]
lo=[]
mn=[]


os.chdir(r"C:\\Users\\satwik bansal\\Desktop")
with open(r"Travel_Times.csv",'r') as file:
    csvreader=csv.reader(file)

    for row in csvreader:
        rows.append(row)
    rows.pop(0)
for i in rows:
    des.append(i[3])
    up.append(i[7])
    lo.append(i[6])
    mn.append(i[5])




root=Tk()

def func():
    a=dis1.get()
    if a not in des:
        messagebox.showinfo("ERROR!!", "WRONG INPUT")
    else:
        dis2.insert(END, lo[des.index(a)])
        dis3.insert(END, up[des.index(a)])
        dis4.insert(END, mn[des.index(a)])

        objects = ["Lower Limit", "Mean Time", "Upper Limit"]
        y_pos = np.arange(len(objects))
        performance = [lo[des.index(a)],mn[des.index(a)],up[des.index(a)]]
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel("Graph")
        plt.show()


def clear():
    dis1.delete(0,END)
    dis2.delete(0,END)
    dis3.delete(0,END)
    dis4.delete(0,END)






dis1 = Entry(root)
dis1.grid(row=1, column=2, sticky=W)
dis2 = Entry(root)
dis2.grid(row=4, column=2)
dis3 = Entry(root)
dis3.grid(row=4, column=3)
dis4 = Entry(root)
dis4.grid(row=4, column=4)



lab1 = Label(root, text = "Enter Destination").grid(row = 1, column = 1)
lab2 = Label(root, text = "Lower Time in Seconds").grid(row = 3, column = 2)
lab3 = Label(root, text = "Upper Limit Time in Seconds").grid(row = 3, column = 3)
lab4 = Label(root, text = "Average Time in Seconds").grid(row = 3, column = 4)



but=Button(root, text="click", command=lambda:func()).grid(row=2,column=3)
but2=Button(root, text="clear", command= lambda : clear()).grid(row=2, column= 4)

mainloop()
