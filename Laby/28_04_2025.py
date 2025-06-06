from turtle import *
import random
import time
'''pd()
left(90)
forward(100)
goto(200,100)
goto(0,0)
goto(200,0)
forward(100)
goto(100,150)
goto(0,100)
goto(200,0)
mainloop()
{
    
}
'''
'''def spiralka(a):
    speed(0)
    for i in range(a):
        circle(2*i,100)
        

spiralka(1000)'''
'''colors = ("violet","red","blue","purple","orange","black","yellow","magenta","cyan","crimson")
colors = list(colors)
def kolko(r,x,y):
    goto(x,y-r)
    x = random.choice(colors)
    color(x)
    colors.remove(x)
    begin_fill()
    circle(r)
    end_fill()
speed(0)
for i in range(10,0,-1):
    kolko(i*30,0,0)
hideturtle()'''
tracer(0)
def wielokoat(x,y,liczbabokow,dlugoscbokow):
    penup()
    goto(x,y)
    begin_fill()
    pendown()
    for i in range(liczbabokow):
        forward(dlugoscbokow)
        left(360/liczbabokow)
    end_fill()
speed(0)



while(True):
    colors = []
    for i in range(1000):
        colors.append('#%06X' % random.randint(0, 0xFFFFFF))        
        color(random.choice(colors))
        bgcolor(random.choice(colors))
        x = random.randint(-300,300)
        y= random.randint(-300,300)
        wielokoat(x,y,random.randint(3,10),random.randint(5,20))
        
    time.sleep(1)
    clear()
