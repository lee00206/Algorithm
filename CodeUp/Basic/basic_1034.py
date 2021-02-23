# 8진 정수를 입력받아 10진수로 출력하기
a = input()
b = []
num = 0

for i in range(len(a)-1, -1, -1):
    b.append(a[i])

for j in range(0, len(b)):
    num = num + (8**j * int(b[j]))

print(num)