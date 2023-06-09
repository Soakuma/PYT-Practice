num = int(input())
count = 0
for _ in range(num):
    word = input()
    if len(word) == 1:
        count += 1
    else:
        current = ""
        seen = []
        for i in range(len(word)):
            if word