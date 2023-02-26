try:
    a = open("name.txt", "r")
    
    print( a.read() )
except FileNotFoundError:
     print("파일이 없습니다.")