f = open( "C:\\Folder\\information.txt", "r" ) #저장된 텍스트 파일에 대한 경로
 
infor = f.readlines() #리스트 단위로 읽어서 저장
 
 
id = input( "아이디를 입력하세요.") # id 부분을 입력받음
pw = input( "비밀번호를 입력하세요.") # pw 부분을 입력받음
 
flag = False
 
for i in range(len(infor)): # 텍스트 파일 내 끝날때까지 반복(여기서는 네 줄이므로 4)
    information = infor[i].split() # infor를 information에 저장. 이때 리스트를 인수 하나하나 쪼개서 저장. 따라서 information도 리스트가 되고, information[0], information[1]에 하나씩 들어간다.
    if information[0] == id and information[1] == pw: # 만약 입력한 id값과 pw 값이 각각 일치하면!(information[0] = 숫자 부분 information[1] = 알파벳 부분)
        flag = True
        break
    else:
        flag = False
 
if flag:
    print( "로그인 성공" )
else:
    print( "로그인 실패" )