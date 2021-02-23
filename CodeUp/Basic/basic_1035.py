# 16진수 정수 1개 입력받아 8진수로 출력하기

a = input()
b = []
list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

# 입력받은 수를 거꾸로 저장
for i in range(len(a)-1, -1, -1):
    b.append(a[i])

# 16진수를 10진수로 변환
c = 0
for j in range(0, len(b)):
    c = c + (16**j * int(list.index(b[j])))

# 10진수를 8진수로 변환
d = []
while c > 8:
    d.append(c % 8)
    c = c // 8

d.append(c)

for k in range(len(d)-1, -1, -1):
    print("{0}".format(d[k]), end = '')
