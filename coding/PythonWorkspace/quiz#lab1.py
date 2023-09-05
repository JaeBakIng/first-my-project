from tkinter import *
from tkinter import messagebox


def click() :
    ent_text = entry.get() #entry 에서 값을 입력받은 값을 ent_text에 저장
    print(ent_text)
    label['fg']=ent_text #entry 에서 받은 택스트를 label 색으로써 쓴다 , label의 색을 바꿔주는코드
    messagebox.showinfo('제목',ent_text+'(으)로 색을 변경 합니다')


win = Tk()
win.resizable(False,False)
win.title('버튼 이벤트 만들기')
label = Label(win, text='아래 빈칸에 택스트(색)를 입력하세요',width=40)
entry = Entry(win, width=40)
button = Button(win, text='확인',width=40,bg='pink',command=click)
label.pack()
entry.pack()
button.pack()

win.mainloop()