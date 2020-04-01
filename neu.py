from tkinter import *

root = Tk()
root.title('Neutral')
root.geometry("225x250")
root.iconphoto(False, PhotoImage(file='neutral.png'))

canvas = Canvas(root, width = 300, height = 300)
file = PhotoImage(file = 'neutral.png')
canvas.create_image(0,0, anchor=NW, image=file)
canvas.pack()



