# 정수 3개 입력받아 가장 작은 수 출력하기
a, b, c = input().split()
my_list = [int(a), int(b), int(c)]
my_list.sort()
print(my_list[0])