import random
list = []

for i in range ( 3 ):
    num = random.randint(1,100)
    list.append(num)

list.sort()
print(list)