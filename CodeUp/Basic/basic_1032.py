# 10진 정수 입력받아 16진수로 출력하기

num = int(input())
sixteen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
a = []

while num > 16:
    b = num % 16
    a.append(sixteen[b])
    num = num // 16

a.append(sixteen[num])

for i in range(len(a)-1, -1, -1):
    print("{0}".format(a[i]), end = '')
