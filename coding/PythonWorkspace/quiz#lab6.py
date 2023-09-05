from tkinter import *
from tkinter import messagebox
win = Tk()
win.title('항공기 운항 프로그램')
win.geometry('300x150')
win.resizable(False,False)


def enter() :
    rain = float(entry.get())
    wind = float(entry2.get())
    if(rain<200 and wind<30):
        messagebox.showinfo('양호','운행이 가능합니다.')
    else :
        messagebox.showinfo('경고','운행이 불가합니다!!')



label = Label(win,text='강수량 입력',font=('',15))
label.pack()
entry = Entry(win,font=('',15))
entry.pack()

label = Label(win,text='풍속 입력',font=('',15))
label.pack()
entry2 = Entry(win,font=('',15))
entry2.pack()


button = Button(win, text='확인' ,command=enter)
button.pack()



win.mainloop()