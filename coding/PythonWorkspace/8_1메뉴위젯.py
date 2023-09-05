from tkinter import *
win = Tk()

def msg () :
    msg1 = Message(win,text='Load')
    msg1.pack()

def quit() :
    win.destroy()

upmenu = Menu(win) #window 창에 메뉴 생성


dnmenu = Menu(upmenu) #upmenu 밑에 하위메뉴 생성
dnmenu2 = Menu(upmenu)


upmenu.add_cascade(label= '종료 메뉴', menu=dnmenu) #cscade로 upmenu와 dnmenu를 합쳐줌
upmenu.add_cascade(label= '상위 메뉴', menu=dnmenu2) 



dnmenu.add_command(label = '하위메뉴 Load',command=msg)
dnmenu.add_command(label = '하위메뉴 quit',command=quit)
dnmenu.add_command(label = '아무것도 아닌 메뉴')


dnmenu2.add_command(label='두번째 하위 메뉴')



win.config(menu=upmenu) # 윈도우에 메뉴가 나타나게 함










win.mainloop()
