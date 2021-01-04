# sampling random points within a circle with radius r
# inverse transofrm sampling
# cdf : F(d) =d**2/r**2
# inverse cdf : r*(u**0.5)

import turtle
# turtle 모듈 : 파이썬에서 기본적으로 제공하는 기본 모듈로 코드에 따라 그림을 그려주는 모듈

import math
import random

wn=turtle.Screen()
turtle.tracer(8,0)
alex=turtle.Turtle()
alex.hideturtle()
r=200

for i in range(5000):
    u=random.random()
    d=r*(u**0.5)
    #d=u*r #dense around the center : 원의 중심에 더 집중적으로 찍히게 됨
    theta=random.random()*360 # 각도도 샘플링
    x=d*math.cos(math.radians(theta))
    y=d*math.sin(math.radians(theta))
    alex.penup()
    alex.setposition(x,y)
    alex.dot()
turtle.update()
wn.mainloop()