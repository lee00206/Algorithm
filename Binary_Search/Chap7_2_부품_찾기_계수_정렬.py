# 계수정렬로 부품 찾기
# 가게의 부품 개수 입력받기
n = int(input())

# 가게의 부품 번호 입력받기
store = list(map(int, input().split()))

# 손님의 부품 개수 입력받기
m = int(input())

# 손님의 부품 번호 입력받기
customer = list(map(int, input().split()))

# 데이터 크기만큼 리스트 만들기
array = [0] * (max(store) + 1)

# 계수 정렬
for i in range(len(store)):
    array[store[i]] += 1

for customer in customer:
    if array[customer] != 0:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

