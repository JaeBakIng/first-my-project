from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('로그인 하세요.')
win.resizable(False,False) #윈도우 좌우 크기 설정 불가능

IDPW = {"시르메":"abc123","스야시카":"abc123","모티":"abc123","민재":"abc123","alswo2817":"te7129un!"}

def check_IDPW() :
    get_id = user_id.get() #user_id 에서 입력된 값을 가져옴
    if get_id in IDPW : #가져온 값이 IDPW 딕셔너리에 있을때 이중 if문
        
        if IDPW[get_id] == user_pw.get(): #IDPW의 아이디(=비밀번호)값(딕셔너리) 과 비밀번호가 일치하면 로그인 성공
            messagebox.showinfo('로그인 성공', get_id +'님 환영합니다.')
            win.destroy()
        else :
            messagebox.showinfo('실패','비밀번호가 일치하지 않습니다')
    else :
        messagebox.showinfo('실패','아이디가 일치하지 않습니다.')


label1 = Label(win,text='ID를 입력하세요')
user_id = Entry(win,width=30)
label2 = Label(win,text='PW를 입력하세요')
user_pw = Entry(win,width=30,show="*")
button = Button(win, text='로그인',width=20 , command=check_IDPW)


label1.pack()
user_id.pack()
label2.pack()
user_pw.pack()
button.pack()

win.mainloop()