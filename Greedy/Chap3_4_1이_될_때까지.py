# 1이 될 때까
# n, k 입력
n, k = map(int, input().split())

# 반복문 수행
count = 0
while Tr지ue:
    if n == 1:
        break
    else:
        if n % k != 0:
            n -= 1
            count += 1
        else:
            n = n / k
            count += 1

print(count)

