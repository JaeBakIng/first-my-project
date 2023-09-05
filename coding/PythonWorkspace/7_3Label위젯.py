from tkinter import *
win = Tk()

label1 = Label(win, text='색상', fg='light yellow',bg='cyan')
label2 = Label(win, text='폰트', font=('궁서체' , 20))
label3 = Label(win, text='anchor=남쪽', height=5 , anchor='s')

label1.pack()
label2.pack()
label3.pack()

win.mainloop()
