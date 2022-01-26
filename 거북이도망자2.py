import turtle as t
import random
from tkinter import *
from tkinter import messagebox

score = 0
playing = False
special = False
shadow = False

# 초기 위치 셋팅

# 내거북이
tt = t.Turtle()
tt.shape("turtle")
tt.color("white")
tt.speed(0)
tt.up()
tt.goto(0,0)

# 악당 거북이
te = t.Turtle()
te.shape("turtle")
te.color("black")
te.speed(0)
te.up()
te.goto(0,200)

# 먹이
fd = t.Turtle()
fd.shape("circle")
fd.color("green")
fd.speed(0)
fd.up()
fd.goto(0,-200)

# 스폐셜 먹이
sfd = t.Turtle()
sfd.shape("circle")
sfd.color("white")
sfd.speed(0)
sfd.up()
sfd.goto(-300,-300)
sfd.hideturtle()

# 그림자거북이
tsd = t.Turtle()
tsd.shape("turtle")
tsd.color("red")
tsd.speed(0)
tsd.up()
tsd.goto(-300,-300)
tsd.hideturtle()

# 내 거북이 움직임 정의
def turn_right():
    tt.setheading(0)

def turn_up():
    tt.setheading(90)

def turn_left():
    tt.setheading(180)

def turn_down():
    tt.setheading(270)

def special_food():
    global special
    start_x3 = random.randint(-100,100)
    start_y3 = random.randint(-100,100)
    tsd.goto(start_x3, start_y3)
    tsd.showturtle()
    sfd.hideturtle()
    special = False

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

# 게임 플레이
def play():
    global score
    global playing
    global special
    global shadow
    start_x4 = 0
    start_y4 = 0

    tt.forward(10)

    # 악당거북이 방향 및 속도 설정
    if random.randint(1,5) == 3 :
        if shadow == True :
            ang = te.towards(tsd.pos())
        else :
            ang = te.towards(tt.pos())
        te.setheading(ang)
    speed = score + 5

    if speed > 15:
        speed = 15
    te.forward(speed)

    # 그림자 거북이 방향 및 속도 설정
    if shadow == True:
        if tsd.xcor() <= 230 and tsd.xcor() >= -230 and tsd.ycor() <= 230 and tsd.ycor() >= -230 :
            if random.randint(1,4) == 1:
                start_x4 = random.randrange(240,250,1)
                start_y4 = random.randrange(-240,240,10)
            elif random.randint(1,4) == 2:
                start_x4 = random.randrange(-250,-240,1)
                start_y4 = random.randrange(-240,240,10)
            elif random.randint(1,4) == 3:
                start_x4 = random.randrange(-240,240,10)
                start_y4 = random.randrange(240,250,1)
            elif random.randint(1,4) == 4:
                start_x4 = random.randrange(-240,240,10)
                start_y4 = random.randrange(-250,-240,1)
            tsd.forward(5)
        else :
            tsd.forward(0)

    # 악당거북이가 내 거북이 잡다
    if tt.distance(te) < 12 :
        text = "Score : " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    # 내 거북이가 먹이를 먹다
    if tt.distance(fd) < 12:
        score = score + 1
        tt.write(score)
        start_x = random.randint(-230,230)
        start_y = random.randint(-230,230)
        fd.goto(start_x, start_y)

        # 스페셜 먹이 생성
        if special == False and shadow == False:
            if random.randint(1,3) == 3:
                special = True
                sfd.showturtle()
                start_x2 = random.randint(-230,230)
                start_y2 = random.randint(-230,230)
                sfd.goto(start_x2, start_y2)

    # 내 거북이가 스페셜 먹이를 먹다
    if tt.distance(sfd) < 12:
        special_food()
        shadow = True

    # 그림자 거북이가 잡히다
    if tsd.distance(te) < 12:
        tsd.hideturtle()
        shadow = False

    # 게임 진행
    if playing == True :
        t.ontimer(play, 100)

    # 경계선 처리
    if tt.xcor() > 250 :
       tt.setx(-250)

    if tt.xcor() < -250 :
       tt.setx(250)

    if tt.ycor() > 250 :
       tt.sety(-250)

    if tt.ycor() < - 250 :
       tt.sety(250)

# 게임 종료 시 메세지
def message(m1, m2) :
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("",20))
    t.goto (0,-100)
    t.write(m2, False, "center", ("",15))
    t.home()

# 게임판 설정
t.title("Turtle Run")
t.setup(500,500)
t.bgcolor("orange")
t.speed(0)
t.up()
t.hideturtle()

# 게임 동작 함수
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")

t.listen()
message("Turtle Run", "Start : [Space]")

# 게임설명서
root = Tk()
root.title("게임규칙")
root.geometry("470x120")
root.resizable(900,900)

txt1 = """1. 방향키로 하얀색 거북이를 이동합니다.
2. 초록색 먹이를 먹으면 점수가 올라갑니다.
3. 가끔 나타나는 하얀색 먹이를 먹으면 가짜 거북이가 악당을 유혹합니다. 
4. 악당(검은색) 거북이에게 잡히지 마세요.

※ 이 게임은 저작권 및 바이러스가 없는 안전한 게임입니다. 가볍게 즐겨주세요.
    (made by HAZEL)
 """

lbl3 = Label(root, justify=LEFT, text = txt1)
lbl3.grid(row=0, column=1)

t.mainloop()
