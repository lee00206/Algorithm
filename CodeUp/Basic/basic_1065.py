# 정수 3개를 입력받아 짝수만 출력
a, b, c = input().split()
my_list = [int(a), int(b), int(c)]

for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        print(my_list[i])