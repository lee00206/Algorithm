# 숫자 카드 게임

# 행열 입력
n, m = map(int, input().split())

# 각 행에서 가장 숫자가 낮은 카드를 찾고 최종적으로 가장 높은 숫자의 카드 뽑기
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)