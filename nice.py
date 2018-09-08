#coding=utf-8
import tkinter as tk
import numpy as np
from PIL import Image
from tkinter import StringVar
window=tk.Tk()
window.title('nice')
window.geometry('350x170')
tk.Label(window, text="nice").grid(row=0,column=1)
tk.Label(window, text="输入图片名").grid(row=1,column=0)
val=StringVar()
enter=tk.Entry(window,textvariable=val).grid(row=1,column=1)
im1=tk.PhotoImage(file='gg.png')
def piu():
    var=val.get()
    typelist='$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`.'
    try:
        img=Image.open(var+'.jpg').convert('L')
    except OSError as reason:
        val.set('错误，请查证后重新输入')
    img.thumbnail((200,200))
    m=np.array(img)
    f=open(var+'.txt','w')
    for n in m:
        for i in n:
            f.write(typelist[int(i/3.76)]+' ')
        f.write('\n')
    f.close()
tk.Label(window, text="按呀").grid(row=2,column=0)
tk.Button(window,image=im1,command=piu).grid(row=2,column=1)
window.mainloop()

