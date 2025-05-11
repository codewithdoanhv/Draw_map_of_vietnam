import turtle
from playsound import *
import os

VN = turtle.Screen()
VN.title("Bản đồ Việt Nam")
VN.register_shape("pen2.gif")
pen = turtle.Pen()
pen.speed(1)
pen.shape("pen2.gif")
pen.penup()

# Vẽ phần đất liền Việt Nam
file = open('vietnam.txt', 'r')
vietnams = file.readlines()
pen.color("red", "red")
count = 0
for vietnam in vietnams:
    viet = vietnam.strip().split()
    pen.goto(float(viet[0]), float(viet[1]))
    if count == 0:
        pen.pendown()
        pen.begin_fill()
        # playsound("haokhivietnam.wav", False)
    count += 1
pen.end_fill()
pen.penup()

# Vẽ sao vàng
file = open('saovang.txt', 'r')
saovangs = file.readlines()
pen.color("yellow", "yellow")
count = 0
for sao in saovangs:
    saovang = sao.strip().split()
    pen.goto(float(saovang[0]), float(saovang[1]))
    if count == 0:
        pen.pendown()
        pen.begin_fill()
        # playsound("saovang.wav", False)
    count += 1
pen.end_fill()
pen.penup()

# Vẽ các đảo
pen.color("red", "red")
pen.pensize(2)
file = open('cacdao.txt', 'r')
cacdao = file.readlines()
file.close()
count = 0
for dao in cacdao:
    count += 1
    d = dao.strip().split(" ")
    pen.goto(float(d[0]), float(d[1]))
    if count %7 == 1:
        pen.pendown()
        pen.begin_fill()
    if count %7 == 0:
        pen.end_fill()
        pen.penup()

# THÊM CHỮ "QUẦN ĐẢO HOÀNG SA" VÀ "QUẦN ĐẢO TRƯỜNG SA"
# Tạo một turtle mới để viết chữ
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("blue")  # Màu chữ

# Viết "Quần Đảo Hoàng Sa" - điều chỉnh tọa độ phù hợp với vị trí đảo
text.goto(230, 30)  # Điều chỉnh tọa độ này theo vị trí thực tế
text.write("QUẦN ĐẢO HOÀNG SA", align="center", font=("Arial", 12, "bold"))

# Viết "Quần Đảo Trường Sa" - điều chỉnh tọa độ phù hợp với vị trí đảo
text.goto(250, -150)  # Điều chỉnh tọa độ này theo vị trí thực tế
text.write("QUẦN ĐẢO TRƯỜNG SA", align="center", font=("Arial", 12, "bold"))

# Thêm dòng khẳng định chủ quyền
text.goto(0, -290)
text.color("red")
text.write("HOÀNG SA, TRƯỜNG SA LÀ CỦA VIỆT NAM", 
           align="center", font=("Arial", 16, "bold"))

pen.hideturtle()
turtle.done()