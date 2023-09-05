def evnt_func(event) : # 이벤트 호출 함수는 괄호 안에 event 필요
    messagebox.showinfo('메시지', '마우스 더블클릭')

win.bind('<Double-Button>', evnt_func)
win.mainloop()
