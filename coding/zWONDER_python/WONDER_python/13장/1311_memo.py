from tkinter import *
from tkinter import filedialog

def open() :                                # 파일열기가 선택되면 실행되는 함수 open
    file = filedialog.askopenfile()
    text.insert('1.0', file.read())             # 1.0 1번 줄 0번째 칸에 삽입
    file.close()

def save() :                                # 저장하기가 선택되면 실행되는 함수 save
    file = filedialog.asksaveasfile()
    file.write(text.get('1.0', END+'-1c'))      # 모든 텍스트 읽어옴
    file.close()

win = Tk()
text = Text(win, width=60, height=20, font=('', 15), bg='#ffffef')
text.pack()

upmenu = Menu(win)                          # 윈도우의 Menu 생성 -> upmenu
dnmenu = Menu(upmenu)                       # upmenu 하위메뉴 생성 -> dnmenu
upmenu.add_cascade(label = '파일', menu = dnmenu)
dnmenu.add_command(label = '파일열기 Open', command = open)
dnmenu.add_command(label = '저장하기 Save', command = save)
win.config(menu = upmenu)                   # 윈도우에 Menu 나타나게 함
win.mainloop()
