from turtle import *
pen1=Pen()
pen2=Pen()

setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'teal')
def star(x,y):
    speed(99)
    
    goto(x,y=None)
    color('red', 'yellow')
    begin_fill()
    for i in range(0,36):
        forward(200)
        left(170)
        
    end_fill()
    done()





onscreenclick(star(x,y))
    
    


