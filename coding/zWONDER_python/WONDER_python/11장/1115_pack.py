from tkinter import *
win = Tk()

button1 = Button(win, text = 'b1', fg = 'light yellow', bg = '#ff0000')
button2 = Button(win, text = 'b2', bd = 5, padx = 20)
img = PhotoImage(file = 'man2.png')
button3 = Button(win, image = img)

button1.pack(side = 'left')                 # 왼쪽부터 위젯 배치됨
button2.pack(side = 'left', fill = 'y')     # y축 윈도우 크기까지 확장
button3.pack(side = 'left')
win.mainloop()
