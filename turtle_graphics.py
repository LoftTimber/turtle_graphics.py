from turtle import *


pen2=Pen()
pen3=Turtle()

setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'skyblue')
def plant(x,y):

    

    
    speed(0)
    points=36
    penup()
    
    goto(x,y)
    
    
    #leafs
    color('green','green')
    width(1)
    
    
    goto(x,y)
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
    penup()
     #stem
    color('lightgreen')
    
    width(10)
    pendown()
    goto(x,-900)
    forward(11.5)
    end_fill()
    penup()
    
    
    
    
    
    
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
    for i in range(0,2):
        pen2.forward(20000)
        pen2.right(90)
        pen2.forward(1000)
        pen2.right(90)
    
    
    pen2.end_fill()
    pen2.ht()

        



def rose(x,y):
    speed(0)
    penup()
    left(0)
    goto(x,y)
    width(1)
    color('black','red')
    pendown()
    left(52.5)
    begin_fill()
    for i in range(0,3):
        right(15)
        for i in range(0,2):
            
             
            
            forward(150)
            right(45)
            forward(150)
            right(135)
            
    end_fill()
    right(97.5)
    ht()
def sunflower(x,y):
    penup()
    right(90)
    
    goto(x,y)
    left(90)
    forward(150)
    color('brown','yellow')
    width(1)
    speed(0)
    pendown()
    begin_fill()
    rt(45)
    
    rt(135)

    
    p=0
    while p<36:

        for i in range(0,6):
            fd(80)
            rt(60)
        rt(10)
        p+=1
    
    end_fill()
    left(90)











dr_p2()
def pick_s(x,y):
        
    
        
    plant(x,y)
    sunflower(x,y)
        
    
    
    

def pick_r(x,y):
    plant(x,y)
    rose(x,y)



onscreenclick(pick_s,btn=3)
onscreenclick(pick_r,btn=1)
















