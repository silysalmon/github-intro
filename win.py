import tkinter
from PIL import Image,ImageTk
win = tkinter.Tk()
win.title("GUI")

im = Image.open('/home/akash/Pictures/Wallpapers/nature-sky-sunset-the-mountains-66997.jpg')
im_tk=ImageTk.Photoimage(im)
lab = tkinter.Label(image=im_tk)
lab.grid(row=0,column=0)

win.mainloop()
