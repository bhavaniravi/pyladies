from turtle import *
import turtle


def shape(sides, length):
    for i in range(sides):
        forward(length)
        right(360/sides)


for i in range(100):
    shape(6, 150)
    right(18)
