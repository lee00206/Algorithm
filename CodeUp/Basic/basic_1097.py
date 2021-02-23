# 바둑알 십자 뒤집기
# 바둑판 값 입력받아 2차원 배열로 저장
board = []
for i in range(0, 19):
    board.append(input().split())

# 십자 뒤집기 횟수 입력받기
n = int(input())

# 십자 뒤집기 좌표 입력받기
location = []
for j in range(0, n):
    location.append(input().split())

# 십자 뒤집기
for k in range(0, n):
    row = int(location[k][0]) - 1   # 좌표 행
    col = int(location[k][1]) - 1   # 좌표 열
    for r in range(0, 19):
        # 좌표 행 바둑알 뒤집기
        if board[row][r] == '1':
            board[row][r] = '0'
        else:
            board[row][r] = '1'

    for u in range(0, 19):
        # 좌표 열 바둑알 뒤집기
        if board[u][col] == '1':
            board[u][col] = '0'
        else:
            board[u][col] = '1'

# 출력
for x in range(0, 19):
    for y in range(0, 19):
        print(board[x][y], end = ' ')
    print()
