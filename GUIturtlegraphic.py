#거북이 기본
#import turtle as t
 
#t.shape( "turtle" )
#t.forward( 50 )
#t.right( 90 )
#t.forward( 50 )
#t.left( 90 )
#t.forward( 50 )
#t.left( 90 )
#t.forward( 50 )

#t.mainloop()

#팬업 팬다운
#import turtle as t
 
#t.pendown()
#t.forward( 50 )
#t.right( 90 )
#t.penup()
#t.forward( 30 )
#t.right( 90 )
#t.pendown()
#t.forward( 50 )

#t.mainloop()

#그리기 속도

#import turtle as t
 
#t.shape( "turtle" )
#t.speed( 3 )
#t.forward( 300 )
 
#t.speed( 1 )
##t.right( 90 )
#t.forward( 300 )
#t.right( 90 )
 
#t.speed( 5 )
#t.forward( 300 )

#t.mainloop()

#거북이 숨기기

#import turtle as t
 
#t.shape( "turtle" )
#t.hideturtle()
 
#t.forward( 200 )

#t.mainloop()

#스탬프

#import turtle as t
 
#t.shape( "turtle" )

#t.forward( 200 )
#t.stamp()
#t.right( 90 )
#t.forward( 100 )

#t.mainloop()

#지우기

#t.clear()
#t.reset()

#원, 호, 다각형 그리기

#import turtle as t
 
#t.shape( "turtle" )
#t.speed( 3 )
#t.circle( 100, 360, 5 )
 
#t.done()

#팬 굵기, 색상

#import turtle as t
 
#t.shape( "turtle" )
 
#t.forward( 50 )
 
#t.pensize( 3 )
#t.forward( 50 )
 
#t.pensize( 1 )
#t.forward( 50 )
 
#t.pencolor( "blue" )
#t.forward( 50 )
 
#t.pencolor( "red" )
#t.forward( 50 )
	
#bgcolor( 색상 )    # 배경 색상을 칠하는 코드
#fillcolor( 색상 )     # 도형 내부 색상을 지정하는 코드
#begin_fill()    # 내부 색상을 칠하는 코드
#end_fill()     # 내부 색상 칠하기를 끝내는 코드

#t.done()

#글씨 색, 배경 색
	
import turtle as t
 
t.shape( "turtle" )
 
t.fillcolor( "yellow" )
 
t.begin_fill()
t.circle( 40 )
t.forward( 100 )
t.end_fill()
 
t.fillcolor( "blue" )
 
t.begin_fill()
t.circle( 40 )
t.end_fill()
 
t.forward( 100 )
t.circle( 40 )
	
 
t.shape( "turtle" )
 
t.bgcolor( "green" )

t.done()