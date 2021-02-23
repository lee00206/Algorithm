# 출석 번호 부르기
n = int(input())
a = [input().split()][0]

my_list = [int(i) for i in a]

my_list.sort()
print(my_list[0])