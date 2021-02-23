# 10진수를 받아 8진수로 변환하여 출력

a = int(input())
b = []

while a > 8:
    b.append(a % 8)
    a = a // 8

b.append(a)

for i in range(len(b)-1, -1, -1):
    print("{0}".format(b[i]), end = '')
    
