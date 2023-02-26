import turtle as t

def moveForward() :
    t.forward( 10 )
 
def turnLeft() :
    t.left( 90 )
 
def turnRight() :
    t.right( 90 )
 
def turnBack() :
    t.right( 180 )
 
def colorRed() :
    t.pencolor( "red" )
 
def colorBlue() :
    t.pencolor( "blue" )
 
def colorGreen() :
    t.pencolor( "green" )

def checkpoint() :
    t.stamp()
    t.ontimer( checkpoint, 10000 )
 
def clearAll( x,y ) :
    t.clear()

def halfcircle() :
    t.circle(10, 180)
 
t.shape( "turtle" )
t.onkeypress( moveForward, "Up" )
t.onkeypress( turnLeft, "Left" )
t.onkeypress( turnRight, "Right" )
t.onkeypress( turnBack, "Down" )
 
t.onkeypress( colorRed, "r" )
t.onkeypress( colorBlue, "b" )
t.onkeypress( colorGreen, "g" )

t.onscreenclick( clearAll )

t.onkeypress(halfcircle, "c")
 
t.ontimer( checkpoint, 10000 )
 
t.listen()
t.done()