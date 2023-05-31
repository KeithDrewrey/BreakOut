import turtle
from turtle import *


game = True

class Ball(Turtle):
    def __init__(self):
        Turtle.__init__(self, shape="circle")
        self.color("white")
        self.pu()
        self.goto(0.00, -200)
        #self.fd
        self.setheading(45)
        self.speed(7)

def pause():
    global game
    game = False

def resume():
    global game
    game = True

def start_ball():
    while game:
        paddle_interaction()
        ball.forward(5)
        heading = ball.heading()
        pos = ball.pos()
        # print(ball.heading())
        # print(ball.pos())

        ##Top & bottom
        if heading <= 89 and pos[1] >= 300:
            ball.setheading(heading - 90)
            print("1")
        elif 90 <= heading <= 180 and pos[1] >= 300:
            ball.setheading(heading + 90)
            print("2")
        elif 181 <= heading <= 270 and pos[1] <= -300:
            ball.setheading(heading - 90)
            print("3")
        elif 271 <= heading <= 360 and pos[1] <= -300:
            ball.setheading(heading + 90)
            print("4")

###Left & Right edges
        elif heading <= 89 and pos[0] >= 350:
            ball.setheading(heading + 90)
            print("5")
        elif 90 <= heading <= 180 and pos[0] <= -350:
            ball.setheading(heading - 90)
            print("6")
        elif 181 <= heading <= 270 and pos[0] <= -350:
            ball.setheading(heading + 90)
            print("7")
        elif 271 <= heading <= 360 and pos[0] >= 350:
            ball.setheading(heading - 90)
            print("8")

def paddle_interaction():
    #while game:
    paddle_pos = paddle.pos()
    ball_head = ball.heading()
    ball_pos = ball.pos()

    v_delta = ball_pos[0] - paddle_pos[0]
    h_delta = ball_pos[1] - paddle_pos[1]
    # print("vert_delta:", v_delta)
    # print("hor_delta:", h_delta)


    if v_delta < 90 and h_delta <30:
        if ball_head > 270:
            ball.setheading(ball_head + 90)
        else:
            ball.setheading(ball_head - 90)






class Paddle(Turtle):
    def __init__(self):
        Turtle.__init__(self, shape="square")
        self.color("white")
        self.pu()
        self.goto(0.00, -200)
        self.speed(9)
        self.shapesize(1, 7, 0)



class Block(Turtle):
    def __init__(self, n, colour, x, y):
        Turtle.__init__(self, shape="square")
        self.color(colour)
        self.pu()
        self.speed(9)
        self.shapesize(1.5, n * 1.5, 0)
        self.goto(x, y)

def move_paddle_right():
    newcoord = paddle.pos()
    newcoord = (newcoord[0]+15, newcoord[1])
    paddle.goto(newcoord)

def move_paddle_left():
    newcoord = paddle.pos()
    newcoord = (newcoord[0]-15, newcoord[1])
    paddle.goto(newcoord)





def create_blocks(row, qty, start, height, stretch, shade, space):
    for i in range(qty):
        row.append(Block(x=(start + (space * i)), y=height, colour=shade, n=stretch))




#write("Block BreakOut - a game by Keith", goto(0,200), font=("Helvetica", 16, "bold"))

row1=[]
row2=[]
row3=[]
create_blocks(row=row1, start=-295, height=150, qty=6, shade = "red", stretch=3.3, space=110)
create_blocks(row=row2, start=-290, height=200, qty=8, shade = "yellow", stretch=2.4, space= 80)
create_blocks(row=row3, start=-300, height=250, qty=7, shade = "blue", stretch=2.9, space= 95)


window = Screen()
# window.bgcolor("black")
window.title("BreakOut")
window.screensize(500, 500, 'black')
ball = Ball()
paddle = Paddle()
# block = Block(3)
onkey(move_paddle_right, "Right")
onkey(move_paddle_left, "Left")
onkey(start_ball, "space")
onkey(pause, "p")
onkey(resume, "r")
listen()




# write("press spacebar to start game",
#       align="center", font=("Courier", 16, "bold"))
# onkey(play, "space")
# listen()


# ball.shape(name = "circle")
# #ball.turtlesize(stretch_wid=1, stretch_len=1)
# ball.color("white")







mainloop()
#
# class Disc(Turtle):
#     def __init__(self, n):
#         Turtle.__init__(self, shape="square", visible=False)
#         self.pu()
#         self.shapesize(1.5, n*1.5, 2) # square-->rectangle
#         self.fillcolor(n/6., 0, 1-n/6.)
#         self.st()
#
# class Tower(list):
#     "Hanoi tower, a subclass of built-in type list"
#     def __init__(self, x):
#         "create an empty tower. x is x-position of peg"
#         self.x = x
#     def push(self, d):
#         d.setx(self.x)
#         d.sety(-150+34*len(self))
#         self.append(d)
#     def pop(self):
#         d = list.pop(self)
#         d.sety(150)
