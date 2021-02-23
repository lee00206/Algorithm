# 두 정수 입력받아 큰 수 출력하기
a, b = input().split()
my_list = [int(a), int(b)]
my_list.sort(reverse = True)
print(my_list[0])