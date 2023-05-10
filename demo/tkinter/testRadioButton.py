import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())

for i in range(ord("A"), ord("D")):
    r = tk.Radiobutton(window, text='Option ' + chr(i),
                        variable=var, value=chr(i),
                        command=print_selection)
    r.pack()

var.set("0")  # 默认一个都没选中
window.mainloop()
