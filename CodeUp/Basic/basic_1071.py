# 0이 될때까지 무한 출력하기
a = []
a.append(input().split())
b = a[0]

for i in range(len(b)):
    if b[i] != '0':
        print(b[i])
    else:
        break