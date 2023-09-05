from tkinter import *
from tkinter import filedialog

def open() :
    file = filedialog.askopenfile()
    text.insert('1.0',file.read())
    file.close()
def save() :
    file = filedialog.asksaveasfile()
    file.write(text.get('1.0',END+'-1c'))
    file.close()
def quit() :
    win.destroy()


win = Tk()

text = Text(win,width=60 , height=20 , font=('',15))
text.pack()

upmenu = Menu(win)
dnmenu = Menu(upmenu)

upmenu.add_cascade(label='파일', menu=dnmenu)
dnmenu.add_command(label='파일 열기', command=open)
dnmenu.add_command(label='저장',command=save)
dnmenu.add_command(label='QUIT',command=quit)

win.config(menu=upmenu)


win.mainloop()