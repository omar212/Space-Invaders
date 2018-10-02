import turtle
import math
import os


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")



#Set Up the screen

border_pen = turtle.Turtle()
border_pen.speed(0) #0 is the fastest
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Create the player turtle

player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15

#Move the player left and right
# When we start the game the player is at x =0 so when we move left
def move_left():
    x = player.xcor()
    x -= playerspeed # takes current value of x subtracts player speed and assigns it to x
    if x < -280:
        x = -280
    player.setx(x)

#pause do it yourself
def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 280:
        y = 280
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #define what global means
    #any changes in this function is refledted everywhere as well
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"  #test it out
    #move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):  # Pythagorean Theorem
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False
#Create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#Create keyboard bindings.
turtle.listen()
turtle.onkey(move_left, "Left") # when i push the left arrow key im going to call the function move left
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

while True:
    #Move the enemy
    #Get the current x cor of the enemy and then add the enemy speed and then we set the x cord to the new x
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemyspeed *= -1    #So we start the game the enemy speed is 2 so to make it come back we need to be -2
        enemy.sety(y)                    #so 2 times -1 is -2
    if enemy.xcor() < -280:
        enemyspeed *= -1    #and then here since enemyspeed is now -2 we need it to +2
        enemy.sety(y)                    #so -2 times -1 is 2

    #Move the bullet
    #we need to get the cur y cor
    if bulletstate == "fire": #save clock cycles
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
        #try

    #check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    #Check for a collision between the bullet and the enemy
    if isCollision(bullet, enemy):
        #Reset the bullet
        bullet.hideturtle()
        bulletstate = "ready"
        bullet.setposition(0,-400)
        #Reset the enemy
        enemy.setposition(-200, 250)

    #End Game
    if isCollision(player, enemy):
        player.hideturtle()
        enemy.hideturtle()
        break;

gameOver = turtle.Pen()
gameOver.pen(fillcolor="black", pencolor="red", pensize=10)
gameOver.pendown()
gameOver.setposition(0,0)
gameOver.write("Game OVER")
gameOver.penup()
gameOver.hideturtle()


turtle.mainloop()  # Always at the end


