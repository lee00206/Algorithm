# 위에서 아래로
# 수의 개수 입력받기
n = int(input())

# 수 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 내림차순으로 정렬
array.sort(reverse = True)

for i in array:
    print(i, end = ' ')