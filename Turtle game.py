import turtle
import math
import random
import time



wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("Playing Game")
wn.bgpic("blue-rose-glitter-animated 1.gif")
wn.tracer(3)


#draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.color("black")
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()
player = turtle.Turtle()
player.color("red")
player.shape("turtle")
player.penup()
player.speed(0)

#create the score variable
Your_Score= 0
High_score= 0


#create goals
maxgoals = 8
goals = []

for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].color("orange")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300,300))


#speed variable 
speed = 1


#define functions
def turnleft():
    player.left(45)
   


def turnright():
    player.right(45)

def increasespeed():
    global speed
    speed +=1   


def decreasespeed():
    global speed
    speed -=2


def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
    
   
#set keyword binding
turtle.listen()
turtle.onkey(turnleft, "Left")

turtle.onkey(turnright, "Right")

turtle.onkey(increasespeed, "Up")


turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)

    #boundary checking
    if player.xcor() >300 or player.xcor() < -300:
        time.sleep(20)
        player.goto(0, 0)
        player.direction = "stop"
       

       
        


    #boundary for y
    if player.ycor() >300 or player.ycor() < -300:
        player.right(180)
        time.sleep(20)
        player.goto(0, 0)
        player.direction = "stop"
    #collision checking

    for count in range(maxgoals):
        goals[count].forward(3)

        if goals[count].xcor() >290 or goals[count].xcor() < -290:
             goals[count].right(180)
        
        #boundary for y
        if goals[count].ycor() >290 or goals[count].ycor() < -290:
             goals[count].right(180)
        

        #collison checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300,300))
            #for moving the goal
            goals[count].right(random.randint(0,360))   
            Your_Score += 10


            #making the score in the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Your_Score: %s" %Your_Score
            mypen.write(scorestring, False, align="left", font=("Arial",14, "normal"))

