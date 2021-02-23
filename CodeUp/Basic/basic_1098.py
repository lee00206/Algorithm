# 설탕과자 뽑기

# 격자판 크기 입력 받기
h, w = input().split()
h, w = (int(h), int(w))

board = [[0 for i in range(w)] for j in range(h)]

# 막대의 개수 입력 받기
n = int(input())

# 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력받기
info = []
for i in range(0, n):
    info.append(input().split())

# 격자판 채우기
for j in range(0, n):
    row = int(info[j][2]) - 1
    col = int(info[j][3]) - 1
    len = int(info[j][0])
    if info[j][1] == '0':
        for k in range(col, col+len):
            board[row][k] = 1
    else:
        for p in range(row, row+len):
            board[p][col] = 1

for x in range(0, h):
    for y in range(0, w):
        print(board[x][y], end = ' ')
    print()