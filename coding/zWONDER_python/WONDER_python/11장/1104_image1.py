from tkinter import *
win = Tk()

img = PhotoImage(file = 'man1.png')     # 이미지를 불러와 img에 저장
label = Label(win, image = img)         # img을 레이블에 넣음
label.pack()                            # .pack(): 레이블 배치
win.mainloop()
