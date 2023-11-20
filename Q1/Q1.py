import turtle


drone = turtle.Turtle()
drone.shape("triangle")
drone.color("blue")
# drone.penup()   # comment it out to get path followed by drone

screen = turtle.Screen()
screen.title("Drone Movement Simulation")
screen.bgcolor("lightgray")
screen.setup(width=800, height=800)  
screen.tracer(0)


def move_forward():
    drone.setheading(90)  
    if drone.ycor() < (screen.window_height() / 2) - 20:
        drone.forward(20)  
    screen.update()

def move_backward():
    drone.setheading(270)  
    if drone.ycor() > -(screen.window_height() / 2) + 20:
        drone.forward(20)  
    screen.update()

def move_left():
    drone.setheading(180)  
    if drone.xcor() > -(screen.window_width() / 2) + 20:
        drone.forward(20)  
    screen.update()

def move_right():
    drone.setheading(0) 
    if drone.xcor() < (screen.window_width() / 2) - 20:
        drone.forward(20)  
    screen.update()


screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

screen.listen()

turtle.exitonclick()
