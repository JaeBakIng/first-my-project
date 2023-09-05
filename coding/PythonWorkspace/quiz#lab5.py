from tkinter import *
win = Tk()
win.title('온도를 입력하세요')
win.geometry('300x100')
win.resizable(False,False)

def enter() :
    Ftemp = float(entry.get())
    Ctemp = (Ftemp-32)/1.8 
    label.config(text='온도='+str('%.1f' % (Ctemp)) + "\'C")

def enter2() :
    Ctemp = float(entry.get())
    Ftemp = (Ctemp*9/5)+32 
    label.config(text='온도='+str('%.1f' % (Ftemp)) + "\'F")


label = Label(win,text='온도 입력',font=('',15))
label.pack()
entry = Entry(win,font=('',15))
entry.pack()
button = Button(win, text='화씨 -> 섭씨' , command=enter)
button2 = Button(win, text='섭씨 -> 화씨',command=enter2)
button.pack(side='left')
button2.pack(side='right')


win.mainloop()

