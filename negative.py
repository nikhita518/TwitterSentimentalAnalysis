import turtle
lion=turtle.Turtle()
lion.up()
lion.goto(0, -100)  
lion.down()

lion.begin_fill()
lion.fillcolor("red")  
lion.circle(100)
lion.end_fill()

lion.up()
lion.goto(-67, -20)
lion.setheading(-60)
lion.width(5)
lion.down()
lion.circle(80, 110)    
lion.fillcolor("black")

for i in range(-35, 105, 70):
    lion.up()
    lion.goto(i, 35)
    lion.setheading(0)
    lion.down()
    lion.begin_fill()
    lion.circle(10)   
    lion.end_fill()
    
lion.hideturtle()
