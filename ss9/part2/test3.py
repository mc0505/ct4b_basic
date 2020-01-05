from turtle import *
import random
color_1 = ["red", "blue", "teal", "green"]
shape("turtle")

round = 0
i = 0
while round <4:
    color(color_1[i])
    i+=1
    forward(100)
    rt(90)
    round +=1


mainloop()