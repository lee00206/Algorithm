# 랜덤 출석번호 부르기
n = int(input())
a = [input().split()][0]

b = [0] * 23

for i in range(len(a)):
    num = int(a[i])
    b[num - 1] = b[num - 1] + 1

for j in range(len(b)):
    print(b[j], end = ' ')