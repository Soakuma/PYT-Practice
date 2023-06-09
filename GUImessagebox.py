#창 띄우기
#from tkinter import *
#import tkinter.messagebox
 
#mainFrame = Tk()
 
#tkinter.messagebox.showerror( "정보 보여주기", "showinfo 대화상자" )
 
#mainFrame.mainloop()
#선택지 창 띄우기
#from tkinter import *
#import tkinter.messagebox
 
#mainFrame = Tk()
 
#result = tkinter.messagebox.askyesno( "정보 보여주기", "대화상자" )
#if result == True :
#    print( "예를 누르셨군요!" )
#elif result == False :
#    print( "아니오를 누르셨군요!" )
# 
#mainFrame.mainloop()
#주관식 선택 창 띄우기
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
 
mainFrame = Tk()
 
result = tkinter.simpledialog.askinteger( "제목", "나이를 입력하세요")
result = tkinter.simpledialog.askinteger( "제목", "비번을 입력하세요")
print( result )
 
mainFrame.mainloop()