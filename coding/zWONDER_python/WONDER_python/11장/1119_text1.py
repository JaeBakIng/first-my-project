from tkinter import *
win = Tk()

text = Text(win, width=50, height=10, font=('', 15), bg='#fffedf')
text.pack()
text.insert(0.0, '1. 첫 번째줄\n2. 두 번째 줄') # 0번째 줄 0번째 문자열 삽입
text.insert(2.4, '2')                           # 2번째 줄 4번째 2 삽입
win.mainloop()
