# 함께 푸는 문제날

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

day = 1

while (day % a != 0) or (day % b != 0) or (day % c != 0):
    day += 1

print(day)