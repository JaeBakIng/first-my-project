from tkinter import *
win = Tk()
win.geometry('300x100')

def name(event) :
    label.config(text='이름:' + svar.get()) #config함수는 label을 새롭게 바꿀때 쓰는함수 4,입력받은 문자열로 label이 바뀜

label = Label(win,text='이름입력',font = ('',15)) # 1,초기상태
label.pack()
svar = StringVar() #문자열 객체 만듦 ,문자열로만 이루어진 값
entry = Entry(win, textvariable = svar, font=('',15)) #문자를 입력받는 이벤트 2,문자열을 입력받아서 svar에 저장
entry.pack()
entry.bind('<Return>',name) #3,엔터치는순간 name함수 호출 
win.mainloop()