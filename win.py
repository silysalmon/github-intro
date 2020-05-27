import tkinter
from PIL import Image,ImageTk
win = tkinter.Tk()
win.title("GUI")
win.geometry("400x400")

def click():
    fra=tkinter.Frame(win,bg="teal",width=100,height=100)
    fra.grid(row=0,column=1)
men=tkinter.Menu(win)
file_men=tkinter.Menu(men,tearoff=0)
men.add_cascade(label="File",menu=file_men)
file_men.add_command(label="Open",command=click)
file_men.add_command(label="Exit",command=click)
im = Image.open('/home/akash/Pictures/Wallpapers/nature-sky-sunset-the-mountains-66997.jpg')
im_tk=ImageTk.Photoimage(im)
lab = tkinter.Label(image=im_tk)
lab.grid(row=0,column=0)

win.config(menu=men)
win.mainloop()
