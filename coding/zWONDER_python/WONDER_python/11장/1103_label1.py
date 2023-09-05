from tkinter import *
win = Tk()
win.geometry('300x200')

label = Label(win, text = 'Lable 만들었음')     # 레이블 위젯 만듦
label.pack()                                    # pack(): win과 결합
win.mainloop()
