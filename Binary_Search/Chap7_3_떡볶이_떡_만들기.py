# 떡볶이 떡 만들기
# 떡의 개수 n과 요청한 떡의 길이 m 값 입력받기
n, m = map(int, input().split())

# 떡의 개별 높이 입력받기
rice = list(map(int, input().split()))

# 이진 탐색
def find_best_value(array, length, start, end):
    """
    반복문을 사용하여 이진 탐색 수행
    """
    result = 0
    while start <= end:
        mid = (start + end) // 2

        rest = []
        for i in range(len(array)):
            if array[i] > mid:
                rest.append(array[i] - mid)

        rest_sum = sum(rest)

        if rest_sum >= length:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

result = find_best_value(rice, m, 0, max(rice))
print(result)