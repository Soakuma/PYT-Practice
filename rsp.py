a= input()
player = a.split()
 
s = player.count('1')
r = player.count('2')
p = player.count('3')
 
if s == 0 and r != 0 and p != 0:
 print(p)
elif s != 0 and r == 0 and p != 0:
 print(s)
elif s != 0 and r != 0 and p == 0:
 print(r)
elif s != 0 and r != 0 and p != 0:
 print(0)
elif s == 0 or r == 0 or p == 0:
 print(0)