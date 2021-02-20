# 이진 탐색으로 부품 찾기
# 가게의 부품 개수 입력받기
n = int(input())

# 가게의 부품 번호 입력받기
store = list(map(int, input().split()))

# 손님의 부품 개수 입력받기
m = int(input())

# 손님의 부품 번호 입력받기
customer = list(map(int, input().split()))

# 데이터 정렬
store.sort()
customer.sort()

# 이진탐색
def binary_search(array, target, start, end):
    """
    재귀함수를 이용한 이진탐색 구현
    """
    if start > end:
        return None

    # 중간점 인덱스
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


for i in customer:
    result = binary_search(store, i, 0, n - 1)
    if result != None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
