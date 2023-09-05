from tkinter import *
win = Tk()

def right(event) : # 키보드 오른쪽 화살표 눌리면 실행되는 함수
    canvas.move(id1, -10, 0)
    canvas.move(id2, 10, 0)
    canvas.move(id3, -5, 0)

def left(event) : # 키보드 왼쪽 화살표 눌리면 실행되는 함수
    canvas.move(id1, 10, 0)
    canvas.move(id2, -10, 0)
    canvas.move(id3, 5, 0)

canvas = Canvas(win, width = 1000, height = 500)
canvas.pack()
png2 = PhotoImage(file = 'man2.png')
png3 = PhotoImage(file = 'man3.png')
png4 = PhotoImage(file = 'man4.png')
id1 = canvas.create_image(500, 100, image = png2)
id2 = canvas.create_image(500, 250, image = png3)
id3 = canvas.create_image(500, 400, image = png4)

win.bind('<Right>', right)
win.bind('<Left>', left)
win.mainloop()
