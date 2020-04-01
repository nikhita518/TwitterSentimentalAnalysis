from tkinter import *
root = Tk()
root.configure(background='black')
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="positive.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()   