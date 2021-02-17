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
first_num = ((m // (k+1)) + (m % (k+1))) * k * first
second_num = (m // (k+1)) * second
result = first_num + second_num

print(result)