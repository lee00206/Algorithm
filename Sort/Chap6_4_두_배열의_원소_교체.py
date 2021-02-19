# 두 배열의 원소 교체
# 배열의 길이 n과 최대 바꿔치기 횟수 k 입력받기
n, k = map(int, input().split())

# 배열 입력받기
array_A = map(int, input().split())
array_B = map(int, input().split())

# A는 오름차순, B는 오름차순으로 정렬
array_A.sort()
array_B.sort(reverse = True)

# A의 최솟값과 B의 최댓값 바꿔치기
for i in range(k):
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else:
        break

# 합 구하기
answer = sum(array_A)
print(answer)