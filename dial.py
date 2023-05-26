word = input()
phone = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0

for c in word:
    for i in range(len(phone)):
        if c in phone[i]:
            time += i + 3
print(time)