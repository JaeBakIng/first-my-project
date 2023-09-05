from tkinter import *

win = Tk()

win.title("윈도우 창")

label = Label(win , text='로또 이미지')
label.pack()

img = PhotoImage(file = 'lotto.png')
#PATH 모듈이 달라서 경로 지정 해줘야댐
label = Label(win, image= img)
label.pack()


win.mainloop()
