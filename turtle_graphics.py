
from turtle import *

pen2=Pen()


setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'skyblue')
def star(x,y):
    speed(0)
    points=36
    penup()
    goto(x,-900)
    pendown()
    color('lightgreen')
    goto(x,0)
    for i in range(0,2):
        left(135)
        forward(100)
    
    color('brown', 'yellow')
    begin_fill()
    for i in range(0,points):
        forward(300)
        left(170)
        
    end_fill()
    ht()
    

x=xcor()
y=ycor()

def dr_p2():
    pen2.color('darkgreen','darkgreen')
    pen2.speed(0)
    pen2.penup()
    pen2.goto(-10000,-900)
    pen2.pendown()
    pen2.begin_fill()
    pen2.forward(20000)
    pen2.right(90)
    pen2.forward(1000)
    pen2.right(90)
    pen2.forward(20000)
    pen2.right(90)
    pen2.forward(1000)
    
    pen2.end_fill()
    pen2.ht()

        



def sunflower(x,y):
    speed(0)
    penup()
    goto(x,-900)
    pendown()
    for i in range(0,4):
        forward(200)
        left(90)
        ht()
def rose(x,y):
    speed(0)
    backward(222)









dr_p2()



onscreenclick(star)
onscreenclick(sunflower,btn=2)
onscreenclick(rose,btn=3)
'''
from turtle import *

def switchupdown(x=0, y=0):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()

def changecolor(x=0, y=0):
    global colors
    colors = colors[1:]+colors[:1]
    color(colors[0])

def main():
    global colors
    shape("turtle")
    resizemode("user")
    shapesize(5)
    width(3)
    colors=["purple", "green", "skyblue", "yellow"]
    color(colors[0])
    switchupdown()
    onscreenclick(goto,1)
    onscreenclick(changecolor,2)
    onscreenclick(switchupdown,3)
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()

import math
#radius=int(input("What is the radius of the flower? "))
#petals=int(input("How many petals do you want? "))
radius=50
petals=15
speed=0

def draw_arc(b,r):  
    c=2*math.pi*r 
    ca=c/(360/60)  
    n=int(ca/3)+1  
    l=ca/n  
    for i in range(n):
        b.fd(l)
        b.lt(360/(n*6))

def draw_petal(b,r):
    draw_arc(b,r)
    b.lt(180-60)
    draw_arc(b,r)

import turtle
bob=turtle.Turtle()

#draw_petal(bob,radius)

for i in range(petals):
    draw_petal(bob,radius)
    bob.lt(360/petals)

turtle.mainloop()
'''

dr_p2()
dr_p3()

penup()
onscreenclick(star)
