# 개미 전사
# 식량창고 개수 입력받기
n = int(input())

# 식량창고에 저장된 식량의 개수 입력받기
k = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 1000

# 보텀업 다이나믹 프로그래밍
d[0], d[1] = k[0], max(k[0], k[1])

for i in range(2, len(k)):
    d[i] = max(d[i - 1], d[i - 2] + k[i])


