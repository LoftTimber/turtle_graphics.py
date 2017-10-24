from turtle import *
pen1=Pen()
pen2=Pen()

setworldcoordinates(-1000,-1000,1000,1000)
screensize(10,10,'teal')
def star():
    speed(99)
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()






pen1
star()
pen2.bk(100)
star()

