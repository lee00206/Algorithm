# 개미 경로
# 상자 입력받기
box = []
for i in range(10):
    box.append(input().split())

# 경로 탐색
row = 1
col = 1

while row < 10:
    if box[row][col] == '0':
        box[row][col] = '9'
        col += 1
    elif box[row][col] == '1':
        col -= 1
        row += 1
    elif col == 9:
        row += 1
    else:
        box[row][col] = '9'
        break

for j in range(0, 10):
    for k in range(0, 10):
        print(box[j][k], end = ' ')
    print()