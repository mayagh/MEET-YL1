import turtle
turtle.speed(0)
turtle.hideturtle()
turtle.shape("turtle")


def draw_square(x,y):
    turtle.color()
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    turtle.end_fill()
draw_square(0,0)

def draw_triangle(x,y):
    turtle.color()
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x+30,y)
    turtle.pendown()
    turtle.goto(x+60,y+100)
    turtle.goto(x+90,y)
    turtle.goto(x+30,y)
    turtle.end_fill()
draw_triangle(20,20)

def switch_filling():
    turtle.color('yellow')

def switch_filling2():
    turtle.color('green')
    

turtle.onscreenclick(draw_square, btn=1, add=True)
turtle.onscreenclick(draw_triangle, btn=3, add=True)
turtle.getscreen().onkeypress(switch_filling, "a")
turtle.getscreen().onkeypress(switch_filling2, "b")
    

turtle.getscreen().listen()    
turtle.mainloop()
