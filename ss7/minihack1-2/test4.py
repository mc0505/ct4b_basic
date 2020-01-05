from turtle import *
shape("turtle")
color("pink")
speed(1)
num = int(input("Nhập số cạnh: "))
loop_count =0
while loop_count < num :
    fd(100)
    rt(360/num)
    loop_count +=1
mainloop()