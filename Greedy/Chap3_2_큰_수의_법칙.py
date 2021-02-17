# 큰 수의 법칙

# 배열의 크기, 숫자가 더해지는 횟수, 연속 최대 횟수 입력
n, m, k = map(int, input().split())

# N개의 자연수 입력
data = list(map(int, input().split()))

# 크기순으로 배열
data.sort(reverse=True)
first = data[0]
second = data[1]

# 합 계산
result = 0        # 결과
count = 0         # 숫자가 더해지는 횟수 카운트
max_count = 0     # 연속 최대 횟수 카운트

while count < m:
    if max_count < k:
        result = result + first
        max_count += 1
        count += 1
    else:
        result = result + second
        max_count = 0
        count += 1

print(result)
