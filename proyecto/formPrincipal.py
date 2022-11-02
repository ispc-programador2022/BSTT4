from tkinter import*

win=Tk()
win.title("Menú Principal")
win.geometry("300x300")
but1= Button(win,text="Tomar Datos html",command=None)
but2= Button(win,text="Salir",command=win.quit)
but1.pack()
but2.pack()
win.mainloop()
