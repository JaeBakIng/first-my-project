from tkinter import *
win = Tk()

def right(event) :
    canvas.move(id1,-10,0)
    canvas.move(id2,10,0)

def left(event) :
     canvas.move(id1,10,0)
     canvas.move(id2,-10,0)

canvas = Canvas(win, width= 1000, height= 500)
canvas.pack()
png1 = PhotoImage(file = 'lotto.png')
png2 = PhotoImage(file = 'abc.png')
id1 = canvas.create_image(500,100,image = png1)
id2 = canvas.create_image(500,250,image = png2)

win.bind('<Right>',right)
win.bind('<Left>',left)
win.mainloop()