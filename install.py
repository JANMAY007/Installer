import os
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=350, bg='gray90', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Type Package:', bg='gray90')
label1.config(font=('helvetica', 14))
canvas1.create_window(150, 80, window=label1)

entry1 = tk.Entry(root, width=27)
canvas1.create_window(150, 120, window=entry1)

install = ""
uninstall = ""


def install_package():
    global install
    install = 'pip install ' + entry1.get()

    os.system('start cmd /k ' + install)


def uninstall_package():
    global uninstall
    uninstall = 'pip uninstall ' + entry1.get()

    os.system('start cmd /k ' + uninstall)


button1 = tk.Button(text='      Install Package    ', command=install_package, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)

button2 = tk.Button(text='   Uninstall Package  ', command=uninstall_package, bg='coral3', fg='white',
                    font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=button2)

root.mainloop()
