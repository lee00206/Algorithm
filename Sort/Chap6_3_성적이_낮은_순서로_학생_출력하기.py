# 성적이 낮은 순서로 학생 출력하기
# 학생 수 입력받기
n = int(input())

# 학생 이름과 성적 입력받기
array = []
for i in range(n):
    array.append(list(input().split()))

# 점수를 기준으로 정렬
array = sorted(array, key = lambda student: int(student[1]))

for student in array:
    print(student[0], end = ' ')