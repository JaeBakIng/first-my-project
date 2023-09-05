from tkinter import *
win = Tk()

def msg() :                 # load 메뉴가 선택되면 실행되는 함수 msg
    msg1 = Message(win, text = 'Load 눌렀냐?')
    msg1.pack()

def quit() :                # quit 메뉴가 선택되면 실행되는 함수 quit
    win.destroy()               # .destroy(): 윈도우 종료

upmenu = Menu(win)          # 윈도우의 Menu 생성 -> upmenu
dnmenu = Menu(upmenu)       # upmenu 하위 메뉴 생성 -> dnmenu
upmenu.add_cascade(label = '상위메뉴', menu = dnmenu)

dnmenu.add_command(label = '하위메뉴 Load', command = msg)
dnmenu.add_command(label = '하위메뉴 Quit', command = quit)
win.config(menu = upmenu)   # 윈도우에 Menu 나타나게 함
win.mainloop()
