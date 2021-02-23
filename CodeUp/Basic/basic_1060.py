# 비트단위로 AND 하여 출력하기

# 정수 입력
a, b = input().split()
num1 = int(a)
num2 = int(b)

# 2진수로 바꾸고 32개로 구성된 리스트 반환
def binary_and_list(num):
    """
    2진수로 바꾸고 32비트 리스트 반환
    """
    binary = bin(num)

    if num > 0:
        num_list = list(binary[2:])
    else:
        num_list = list(binary[3:])

    while len(num_list) <= 32:
        num_list.insert(0, '0')

    if num < 0:
        for i in range(len(num_list)):
            if num_list[i] == '0':
                num_list[i] = '1'
            else:
                num_list[i] = '0'

    return num_list

num1_list = binary_and_list(num1)
num2_list = binary_and_list(num2)

# 논리연산자
new_list = []

for j in range(len(num1_list)):
    if (num1_list[j] == '1') and (num2_list[j] == '1'):
        new_list.append('1')
    else:
        new_list.append('0')

new_list = ''.join(new_list)
new_list = str(int(new_list))
new_list = '0b' + new_list

new_num = int(new_list, 2)

print(new_num)