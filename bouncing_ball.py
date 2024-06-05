import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Bouncing Ball Animation")
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates for smooth animation

# Ball properties
ball = turtle.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.speed(0)  # Fastest drawing speed

# Initial position (randomly within bounds)
ball.setx(random.randint(-390, 390))
ball.sety(random.randint(-290, 290))

# Initial velocity
ball.dx = random.uniform(1, 3)  # Change in x
ball.dy = random.uniform(1, 3)  # Change in y

# Gravity (affects the y velocity)
gravity = 0.1

# Update ball position
def update_position():
    global gravity

    # Update velocity with gravity
    ball.dy -= gravity
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Bounce off the bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverse the direction
        ball.dy *= 0.9  # Simulate energy loss

    # Bounce off the top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse the direction

    # Bounce off the right
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1  # Reverse the direction

    # Bounce off the left
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1  # Reverse the direction

# Animation loop
def animate():
    update_position()  # Update the ball's position
    screen.update()    # Redraw the screen
    screen.ontimer(animate, 20)  # Schedule the next animation frame

# Start the animation
animate()

# Keep the window open
screen.mainloop()
