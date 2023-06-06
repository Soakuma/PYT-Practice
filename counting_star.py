num = int(input())

for i in range(num):
    print(" " * ((num-1)-i) + "*" * (2*i+1))
#crazy python
for i in range(num - 2, -1, -1):
    print(" " * ((num - 1) - i) + "*" * (2 * i + 1))
#math
for i in range(num - 1):
    print(" " * (i+1) + "*" * (((num-1) * 2 - 1) - 2 * i))