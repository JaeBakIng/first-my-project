from tkinter import *
win = Tk()

var1 = IntVar() # IntVar() 정수형 객체 만듦
var2 = IntVar() # IntVar() 정수형 객체 만듦
cb1=Checkbutton(win, text='하와이', variable=var1, onvalue=1,
offvalue=0)
cb2=Checkbutton(win, text='이태리', variable=var2, onvalue=1,
offvalue=0)
cb1.pack()
cb2.pack()
win.mainloop()

print(var1.get()) # 정수값 가져옴
print(var2.get()) # 정수값 가져옴
