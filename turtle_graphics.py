from turtle import *

pen2=Pen()
'''
rt(45)
fd(90)
rt(135)

down()
while x<120:

for i in range(0,6):
    fd(200)
    rt(61)
rt(11.1111)
x=x+1
'''

setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'skyblue')
def star(x,y):

    

    
    speed(0)
    points=36
    penup()
    goto(x,y)
    pendown()
    #leafs
    color('green','green')
    width(1)
    begin_fill()
    for i in range(0,2):
        left(135)
        forward(100)
        left(45)
        forward(100)
    for i in range(0,2):
        forward(100)
        left(45)
        forward(100)
        left(135)
    end_fill()
    left(90)
    #flower
    color('brown', 'yellow')
    begin_fill()
    for i in range(0,points):
        forward(300)
        left(170)
        
    end_fill()
    right(90)
    #stem
    color('lightgreen')
    
    width(10)
    goto(x,-900)
    forward(11.5)
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
    penup()
    goto(x,y)
    color('brown','yellow')
    width(1)
    speed(0)
    pendown()
    begin_fill()
    rt(45)
    
    rt(135)

    
    p=0
    while p<21:

        for i in range(0,6):
            fd(100)
            rt(61)
        rt(11.1111)
        p+=1
    
    end_fill()
    left(180)







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
