import turtle
import time

window = turtle.Screen()
window.bgcolor("white")
wugui = turtle.Turtle()
wugui.shape("turtle")
wugui.color("green")
wugui.circle(60)
wugui.speed(5)
wugui.forward(100)
wugui.right(90)
wugui.forward(100)
color_list = ["red", "white", "blue", "black", "green", "pink"]
for i in color_list:
    time.sleep(1)
    window.bgcolor(i)
'''
for i in range(120):
    wugui.forward(100)
    wugui.right(90)
    wugui.forward(100)
    wugui.right(90)
    wugui.forward(100)
    wugui.right(90)
    wugui.forward(100)
    wugui.right(93)
    time.sleep(0.01)
'''
window.exitonclick()
