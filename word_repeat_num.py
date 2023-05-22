for i in range(int(input())):
    num, word = input().split()
    num = int(num)
    for c in word:
        print(c * num, end="")
    print()