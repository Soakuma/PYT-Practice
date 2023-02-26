#from tkinter import *
 
#mainFrame = Tk()
#mainFrame.geometry( '400x300' )
 
#lbl = Label(mainFrame)
#lbl["text"] = "위치"
 
#def button1(  ) :
#    lbl["text"] = "왼쪽"
 
#def button2(  ) :
#    lbl["text"] = "오른쪽"
#btn1 = Button( mainFrame, text = "왼쪽", command = button1 )
#btn2 = Button( mainFrame, text = "오른쪽", command = button2 )
 
#lbl.pack()
#tn1.pack( side = "left" )
#btn2.pack( side = "right" )
 
#mainFrame.mainloop()

from tkinter import *

mainFrame = Tk()
mainFrame.geometry( '400x300' )

shape = Menu(mainFrame)

mainFrame.config( menu = shape )

shapeitem = Menu(shape)
shape.add_cascade(label = "도형", menu = shapeitem)

helpitem = Menu(shape)
shape.add_cascade(label="정보", menu = helpitem)

shapeitem.add_command( label = "원" )
shapeitem.add_command( label = "사각형" )
shapeitem.add_command( label = "선" )
helpitem.add_command( label = "정보" )
helpitem.add_command( label = "확인" )

Lb = Label(mainFrame, text="로그인 프로그램", font="Serif 20")

import tkinter.messagebox
import tkinter.simpledialog

def login():
    id = tkinter.simpledialog.askinteger( "로그인", "id를 입력 하세요")
    pw = tkinter.simpledialog.askstring( "로그인", "비밀번호를 입력하세요")
    if id == 1 and pw == "a":
        print("환영합니다")
    else:
        print("정보가 옳지 않습니다")

b = Button( mainFrame, text="로그인", command=login)

Lb.pack()
b.pack()

mainFrame.mainloop()