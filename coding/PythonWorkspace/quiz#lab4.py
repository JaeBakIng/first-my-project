from tkinter import *
win = Tk()
win.title("BMI계산기")
def ok() :
    m = int(t.get()) / 100
    bmi = round(int(k.get()) / (m*m), 2)

    if bmi > 29.9 :
        c.config(bg='pink',fg='red',font='bold')
    elif bmi >= 26:
        c.config(bg='yellow',fg='blue',font='bold')
    elif bmi>=18.5:
        c.config(bg='beige',fg='black',font='bold')
    else :
        c.config(bg='gray',fg='black')

        #비엠아이 수치에 따른 색 변경

    c.delete(0,END) # 1, 0인덱스 부터 끝까지 delete 하고
    c.insert(0,'당신의 BMI 지수는 %s' % bmi) # 2, 0의 인덱스에 뒤 텍스트 집어넣음


tall = Label(win, text='키(cm)')
kg = Label(win, text='몸무게(kg)')

t = Entry(win)
k = Entry(win)

button = Button(win,text='BMI 수치 계산', command=ok)

tall.grid(row=0,column=0)
kg.grid(row=0, column=1)
t.grid(row=1,column=0)
k.grid(row=1,column=1)
button.grid(row=2,column=0 , columnspan=2 , ipadx=80)

c = Entry(win,text='결과')
c.grid(row=3,column=0 ,columnspan=2,ipadx=40)

win.mainloop()