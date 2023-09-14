N = int(input())

subject = list(map(int, input().split()))
aver = 0

for i in subject:
    aver = aver + i / max(subject) * 100

print(aver / N)




