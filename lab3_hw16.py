#Alyona Karmazin
#2/13/19
#this program draws

import turtle
tim = turtle.Turtle()
m1 = input("Please enter a number 1: ")
m2 = input("Please enter a number 2: ")
m3 = input("Please enter a number 3: ")
m4 = input("Please enter a number 4: ")
m5 = input("Please enter a number 5: ")
num1 = int(m1)
num2 = int(m2)
num3 = int(m3)
num4 = int(m4)
num5 = int(m5)
for i in range(1):
    tim.forward(100)
    tim.left(num1)
    tim.forward(100)
    tim.left(num2)
    tim.forward(100)
    tim.left(num3)
    tim.forward(100)
    tim.left(num4)
    tim.forward(100)
    tim.left(num5)
    tim.forward(100)

