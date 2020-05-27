import tkinter
from PIL import Image
win = tkinter.Tk()
win.title("GUI")

im = Image.open('/home/akash/Pictures/Wallpapers/nature-sky-sunset-the-mountains-66997.jpg')
lab = tkinter.Label(image=im)
lab.grid(row=0,column=0)

win.mainloop()
