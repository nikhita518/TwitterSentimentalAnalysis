from tkinter import *

root = Tk()
root.title('Negative')
root.geometry("225x250")
root.iconphoto(False, PhotoImage(file='negative.png'))

canvas = Canvas(root, width = 300, height = 300)
file = PhotoImage(file = 'negative.png')
canvas.create_image(0,0, anchor=NW, image=file)
canvas.pack()


