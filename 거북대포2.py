import turtle as t
import random

from tkinter import *
from tkinter import messagebox

from time import *

global cnt
global yn
global time_start
global time_last
global sw

time_start = time()
cnt = 1
sw = 0

root = Tk()
root.title("사용법")
root.geometry("400x130")
root.resizable(0,0)

def your_name():
    global yn
    yn = txt.get()
    # lbl2.configure(text="your name: " + yn)
    root.destroy()

txt1 = """1. 방향키로 이동 및 각도를 조정하세요
2. 스페이스바를 눌러 발사하세요
 """

lbl3 = Label(root, justify=LEFT, text = txt1)
lbl3.grid(row=0, column=1)

lbl = Label(root, text = "                사용자 이름 : ", font = "NanumGothic 8",)
lbl.grid(row=1, column=0)

txt = Entry(root)
txt.grid(row=1, column=1)

btn = Button(root, text ="OK", command = your_name, width=3, height=1)
btn.grid(row=2, column=1)

# lbl2 = Label(root, text ="your name : ")
# lbl2.grid(row=4, column=1)

root.mainloop()

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def move_right():
    (x,y) = t.position()
    t.goto(x+1,y)
    if t.xcor() > -100 or t.xcor() < -250 :
        messagebox.showerror("경고", "쳇, 더이상 갈 수 없군")

def move_left():
    (x,y) = t.position()
    t.goto(x-1,y)

def fire():
    global cnt
    global yn
    global sw
    global time_start
    global time_last
    time2 = time()
    # messagebox.showinfo("time2", "%d" % time2)
    if sw == 0:
        time1 = time_start
    else :
        time1 = time_last
    sw = 1
    # messagebox.showinfo("time1", "%d" % time1)
    et = time2 - time1
    time_last = time2
    # messagebox.showinfo("time_last", "%d" % time_last)
    # messagebox.showinfo("et", "%d" % et)
    if et <= 1:
        messagebox.showerror("경고", "1초 이내 연속발사 기능은 돈을 내야 합니다.")
        return
    # ang = t.heading()
    while t.ycor() > 0:
        t.forward(15)
        t.right(5)
    d = t.distance(target, 0)
    t.hideturtle()
    # t.sety(100)
    t.sety(random.randint(10, 100))
    if d < 15:
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)
        t.showturtle()
        t.setheading(random.randint(0,90))
        if cnt == 1:
            messagebox.showinfo("BEST", "대박!! %s 님은 신의 경지!!." % yn)
        msg1 = str(yn + " 님! " + str(cnt) + " 번 만에 성공했습니다.")
        messagebox.showinfo("RESULT", msg1)
        # messagebox.showinfo("RESULT", "%d 번 만에 성공하셨습니다." % cnt)
        t.onclick(t.clearscreen())
    else:
        words = ["바보ㅋㅋ", "실망스럽군","이게 어렵나?", "나때는 말이아", "우습게 보지 말라고", "할말이 없음"]
        words_select = random.choice(words)
        t.color("red")
        # stamp1=t.stamp()
        t.write( words_select , False, "center", ("", 8))
        # t.write("바보ㅋㅋ", False, "center", ("", 15))
        # t.clearstamp(stamp1)
        t.color("black")
        t.goto(random.randint(-240, -150), 10)
        t.showturtle()
        t.setheading(random.randint(0, 90))
        cnt = cnt + 1

t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(50, 200)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 15, 2)
t.down()
t.goto(target + 15, 2)

t.color("black")
t.up()
t.goto(random.randint(-240, -150), 10)
t.setheading(random.randint(0,90))
t.shape("turtle")

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(move_right, "Right")
t.onkeypress(move_left, "Left")
t.onkeypress(fire, "space")
t.listen()
t.mainloop()
