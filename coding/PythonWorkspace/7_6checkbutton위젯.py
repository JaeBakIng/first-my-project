from tkinter import *
win = Tk()

var1=IntVar() #정수형 객체만듦
var2=IntVar()

cb1=Checkbutton(win,text='하와이',variable=var1,onvalue=1,offvalue=0) #여기서 1,0 의 숫자값을 받기위해서 정수형 객체를 만듦
cb2=Checkbutton(win,text='이태리',variable=var2,onvalue=1,offvalue=0)


cb1.pack()
cb2.pack()
win.mainloop()

print(var1.get())
print(var2.get())
