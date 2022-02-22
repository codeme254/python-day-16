# object oriented programming in python
#  How to use oop: consider what it HAS: and what it DOES:
# an object is just a way of combining some piece of data(attributes) and some functionality(methods) all together in the same thing
# a class is a blue print of an object
# classes are written in PascalCase
from turtle import Turtle, Screen

# creating a new object from the Turtle class
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("crimson")
timmy.speed(1)
timmy.forward(300)
timmy.setheading(90)
timmy.forward(300)
timmy.setheading(60)
timmy.forward(300)
timmy.home()

my_screen = Screen()
# tapping attributes
print(my_screen.canvheight, my_screen.canvwidth)
# tapping methods
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'
print(table)
