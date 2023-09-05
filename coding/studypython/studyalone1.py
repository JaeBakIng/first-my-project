from tkinter import *
win = Tk()
win.title('BMI 계산기')

def click():
    m = int(tl.get())/100
    bmi = round(int(kg.get())/(m*m),2)

    csion.delete(0,END)
    csion.insert(0,'당신의 BMI 수는 %d' % bmi)


label1 = Label(win,text='키(cm)')
label1.grid(row=0,column=0)
label2 = Label(win,text='몸무게(kg)')
label2.grid(row=0,column=1)

tl = Entry(win)
kg = Entry(win)
tl.grid(row=1,column=0)
kg.grid(row=1,column=1)

btn = Button(win,text='BMI 측정',command=click)
btn.grid(columnspan=2 , ipadx=80)
csion = Entry(win)
csion.grid(row=3 ,column=0 , columnspan=2, ipadx=40)


win.mainloop()