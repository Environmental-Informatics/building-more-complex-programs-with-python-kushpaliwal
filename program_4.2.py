"""
Created on January  25, 2020
by Kush Paliwal

Think Python 2e Exercise 4.2
This program creates 3 flowers using turtle
"""

# import libraries
import math
import turtle

# Create line
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

# Create arc
def arc(t, r, angle):
    arc_len = 2 * math.pi * r * angle / 360
    n = int(arc_len / 3) + 1
    step_len = arc_len / n
    step_angle = float(angle) / n
    polyline(t, n, step_len, step_angle)

# Create single leaf
def leaf(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.rt(180-angle)

# Draw flower (arguments: tutrle object, no of petals, radius, angle)
def flower(t, n, r, angle):
     for i in range(n):
        leaf(t, r, angle)
        t.rt(360.0/n)

# Prevent overlapping of flowers (move starting point of turtle without trace)
def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

# Create turtle object
t = turtle.Turtle()

# Flower 1
move(t, -100)
flower(t, 7, 50.0, 60.0)

#Flower 2
move(t, 100)
flower(t, 10, 50.0, 80.0)

#Flower 3
move(t, 100)
flower(t, 20, 120.0, 20.0)