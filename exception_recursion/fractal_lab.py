
#Turtle Recursion (25pts)
import turtle
#1)  Using the turtle library, create the H fractal pattern according to the file shown in the data folder. (10pts)  
'''
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_turtle.shape("turtle")
my_turtle.width(4)
my_turtle.speed(0)

def h_pattern(x, y, height, depth):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()
    my_turtle.setheading(0)

    my_turtle.forward(height)
    my_turtle.backward(height * 2)
    my_turtle.setheading(90)

    my_turtle.forward(height)
    pos1 = my_turtle.pos()

    my_turtle.setheading(270)
    my_turtle.forward(height * 2)
    pos2 = my_turtle.pos()

    my_turtle.setheading(90)
    my_turtle.forward(height)
    my_turtle.setheading(0)
    my_turtle.forward(height * 2)
    my_turtle.setheading(90)
    my_turtle.forward(height)
    pos3 = my_turtle.pos()

    my_turtle.setheading(270)
    my_turtle.forward(height * 2)
    pos4 = my_turtle.pos()

    my_turtle.setheading(90)
    my_turtle.forward(height)
    my_turtle.setheading(180)
    my_turtle.forward(height * 2)

    if depth > 0:
        h_pattern(pos1[0],pos1[1], height / 2 , depth - 1)
        h_pattern(pos2[0], pos2[1], height / 2, depth - 1)
        h_pattern(pos3[0], pos3[1], height / 2, depth - 1)
        h_pattern(pos4[0], pos4[1], height / 2, depth - 1)





h_pattern(0,0, 150, 4)

my_screen.exitonclick()
'''
#2)  Using the turtle library, create any of the other recursive patterns in the data folder. 
#  Challenge yourself to match your pattern as closely as you can to the image.  (10pts)
#  Note:  The Koch snowflake shows step by step building of the fractal.  
#  The rectangle fractal example shows 4 possible drawings of the same fractal (choose any one)
my_turtle = turtle.Turtle()
my_screen = turtle.Screen()
my_turtle.shape("turtle")
my_turtle.width(4)
my_turtle.speed(0)

def square_pattern(x, y, height, depth):
    my_turtle.penup()
    my_turtle.goto(0,0)
    my_turtle.pendown()
    my_turtle.setheading(90)


    my_turtle.forward(height)
    my_turtle.right(90)
    pos1 = my_turtle.pos()
    my_turtle.forward(height)
    my_turtle.right(90)
    pos2 = my_turtle.pos()
    my_turtle.forward(height)
    my_turtle.right(90)
    pos3 = my_turtle.pos()
    my_turtle.forward(height)
    my_turtle.right(90)
    pos4 = my_turtle.pos()

    if depth > 0:
        square_pattern(pos1[0], pos1[1], height / 1.5, depth - 1)
        square_pattern(pos2[0], pos2[1], height / 1.5, depth - 1)
        square_pattern(pos3[0], pos3[1], height / 1.5, depth - 1)
        square_pattern(pos4[0], pos4[1], height / 1.5, depth - 1)


square_pattern(-50,-400, 400, 4)
my_screen.exitonclick()

#3)  Create your own work of recursive art with a repeating pattern of your making (or choose another one from the files).  
#  It must be a repeated pattern using recursion (not just loops). Snowflakes, trees, and spirals are a common choice.  
#  Play around and have fun with it.  (5pt) 

#  General expectations for all problems
#  Give all your fractals a depth of at least 4.  (Don't make programs that take forever though)  
#  Ensure the recursive drawing is contained on the screen (at whatever size you set it).
#  All three recursive drawings can be on the same program.  Just use screen.clear() between problems.  Alternately, you could draw to three different screen objects.
#  Run your turtles at max speed.
#  Have fun!
 
#  Resource to help you out >>> https://docs.python.org/3.3/library/turtle
