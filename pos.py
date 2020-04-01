from tkinter import *

root = Tk()
root.title('Positive')
root.geometry("250x250")
root.iconphoto(False, PhotoImage(file='positive.png'))

canvas = Canvas(root, width = 300, height = 300)
file = PhotoImage(file = 'positive.png')
canvas.create_image(0,0, anchor=NW, image=file)
canvas.pack()

