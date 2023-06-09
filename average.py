n = int(input())

for i in range(n):
    num = list(map(int, input().split()))
    scores = num[1:]
    average = sum(scores)/num[0]
    count = 0
    for score in scores:
        if score > average:
            count += 1
    print(f"{count/num[0] * 100:.3f}%")