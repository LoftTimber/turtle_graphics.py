from turtle import *
pen1=Pen()
pen2=Pen()
pen3=Pen()

setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'teal')
def star(x,y):
    speed(99)
    points=1
    
    goto(x,y)
    pendown()
    color('red', 'yellow')
    begin_fill()
    for i in range(0,points):
        forward(200)
        left(360/points)
        
    end_fill()
    penup()
    

x=xcor()
y=ycor()

def dr_p2():
    pen2.speed(0)
    pen2.goto(0,-1000)
    pen2.forward(1000)
    for i in range(0,4):
        forward(200)
        left(90)

def dr_p3():
    pen3.speed(0)
    pen3.goto(0,-1000)
    pen3.back(1000)
    

dr_p2()
dr_p3()

penup()
onscreenclick(star)
