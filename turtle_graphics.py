from turtle import *
import time

#Turtles
ground_pen=Pen()
sun_pen=Pen()

setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'skyblue')


def draw_plant(x,y):
       
    speed(0)
    penup()      
    color('green','green')
    width(1)
    goto(x,y)

    #draws leafs
    begin_fill()
    left(135)
    for i in range(0,2):
        right(135)
        for i in range(0,2):
            left(135)
            forward(100)
            left(45)
            forward(100)
    end_fill()
    left(225)
    penup()

    #draws stem
    color('lightgreen')
    width(10)
    pendown()
    goto(x,-900)
    forward(11.5)
    end_fill()
    penup()
    
    ht()
    


def draw_ground():
    ground_pen.color('darkgreen','darkgreen')
    ground_pen.speed(0)
    ground_pen.penup()
    ground_pen.goto(-10000,-900)
    ground_pen.pendown()
    
    #draws ground
    ground_pen.begin_fill()      
    for i in range(0,2):  
        ground_pen.forward(20000)
        ground_pen.right(90)
        ground_pen.forward(1000)
        ground_pen.right(90)   
    ground_pen.end_fill()

    ground_pen.ht()

        

def draw_rose_petals(x,y,r_1,r_2):
    speed(0)
    penup()
    goto(x,y)
    width(1)
    color(r_1,r_2)
    pendown()
    left(52.5)
    
    #draws roses petals
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


    
def draw_sunflower_petals(x,y):
    penup()
    goto(x,y)
    forward(150)
    color(sunflower_color,other_sunflower_color)
    width(1)
    speed(0)
    pendown()
    begin_fill()
    rt(180)
    
    #draws sunflower petals
    for i in range(0,36):
        for i in range(0,6):
            fd(80)
            rt(60)
        rt(10)            
    end_fill()
    
    left(90)



def draw_sunflower(x,y):   
    draw_plant(x,y)
    draw_sunflower_petals(x,y)
        


def draw_rose(x,y):        
    draw_plant(x, y)
    draw_rose_petals(x, y, rose_color, other_rose_color)

    

def toggle_color():
    global rose_color, other_rose_color
    global sunflower_color, other_sunflower_color
    rose_color, other_rose_color = other_rose_color, rose_color
    sunflower_color, other_sunflower_color = other_sunflower_color, sunflower_color



    
    
    
    

def draw_sun():
    sun_pen.color('yellow','darkorange')
    sun_pen.penup()
    sun_pen.goto(-1500,1000)
    sun_pen.pendown()

    #draw sun
    sun_pen.begin_fill()
    points=10
    for i in range(0,points):
        sun_pen.forward(1000)            
        sun_pen.rt(1080/points)
    sun_pen.end_fill()
    
    sun_pen.ht()



rose_color = 'white'
other_rose_color = 'red'
sunflower_color='brown'
other_sunflower_color='yellow'
x=xcor()
y=ycor()

#draws ground
draw_ground()

#draws sun and moon
draw_sun()

#listens for keypressing
listen()

#changes colors
onkey(toggle_color, "space")



#draws flowers
onscreenclick(draw_sunflower,btn=3)
onscreenclick(draw_rose,btn=1)











