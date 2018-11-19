#!/usr/bin/env python3

"""Foobar.py: Description of what foobar does.

__author__ = "Zhangyinuo"
__pkuid__  = "1800011770"
__email__  = "1800011770@pku.edu.cn"
"""

import turtle
import math

turtle.screensize(800,600,'black')

sun=turtle.Turtle()
mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()
"""preparations before the planets run
    """


def preparation(t,color,distance,size):
	t.shape('circle')
	t.color(color)
	t.speed(0)
	t.shapesize(size)
	t.up()
	t.forward(distance) 
	t.down()
"""preparations before the planets run
    """

def run():
	for i in range (1,100000):
		a_=[19.35,36.17,55,76.18,260,479]
		a=a_[i%6]
		e_=[0.2056,0.00677,0.01671,0.0934,0.0489,0.0565]
		e=e_[i%6]
		b=a*math.sqrt(1-e**2)
		planet=[mercury,venus,earth,mars,jupiter,saturn]
		pl=planet[i%6]
		angle=[0.4152,0.1625,0.1,0.05319,0.00843,0.003395]
		an=angle[i%6]*i
		pl.goto(a*math.cos(math.radians(an))+a*e,b*math.sin(math.radians(an)))

"""let the planets run
    """
def main():
	preparation(sun,'red',0,1)
	preparation(mercury,'blue',23.33,0.25)
	preparation(venus,'yellow',36.41,0.75)
	preparation(earth,'green',55.92,0.75)
	preparation(mars,'gold',83.30,0.5)
	preparation(jupiter,'coral',272.71,2.5)
	preparation(saturn,'brown',506.2,2)
	run()
"""preparations and run
    """
if __name__ == '__main__':
    main()