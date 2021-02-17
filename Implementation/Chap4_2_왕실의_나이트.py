# 왕실의 나이트

# 좌표 입력
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 움직일 수 있는 방법
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 가능성 세기
count = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if ((next_row >= 1) and (next_row < 9)) and ((next_col >= 1) and (next_col < 9)):
        count += 1

print(count)

