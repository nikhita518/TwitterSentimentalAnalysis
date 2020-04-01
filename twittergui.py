from tkinter import *
import sentiment
import tkinter.messagebox
def twitter():
    try:
        input1 = e1.get()
        if len(input1) == 0:
            raise Exception
        res = sentiment.main(input1)
        positive = res[0]
        negative = res[1]
        neutral = res[2]
        s = 'Positive: '+str(positive)+'% Neutral: '+str(neutral)+'% Negative: '+str(negative)+'%'
        result.set(s)
    except Exception:
        tkinter.messagebox.showerror("Error!","Enter the input in the dailog box")




root = Tk()
root.title("Twitter Sentimental Analysis")
root.geometry("750x600")
root.iconphoto(False, PhotoImage(file='positive.png'))

canvas = Canvas(root, bg='white', width = 750, height = 350)
file = PhotoImage(file = 'sentiment.png')
canvas.create_image(50,20, anchor=NW, image=file)
canvas.pack()

frame = Frame(root, bg='white', width = 750, height = 350)

label1 = Label(frame, text='Enter a domain you want to search', width=30, height=2, bg='white',font=('Verdana',10,'bold')).place(x=20,y=40)

e1 = Entry(frame)
e1.place(x=400,y=50)

button1 = Button(frame, text='Check Result', width = 15, height = 2, bg = 'white',command = twitter).place(x=350,y=100)

result = StringVar()
result.set('')

Label(frame,textvariable=result,fg='black',bg='white',padx=50).place(x=200,y=200)

frame.pack()
root.mainloop()