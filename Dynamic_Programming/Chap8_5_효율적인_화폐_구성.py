# 효율적인 화폐 구성
# n가지 종류의 화폐와 합 m 입력받기
n, m = map(int, input().split())

# 화폐 가치 입력받기
money = []
for i in range(n):
    money.append(int(input()))

# dp 테이블 초기화
d = [10001] * (m + 1)   # 10001은 m을 만드는 방법이 존재하지 않는 경우

# 보텀업 다이나믹 프로그래밍
d[0] = 0

for i in range(n):
    for j in range(money[i], m + 1):
        d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])