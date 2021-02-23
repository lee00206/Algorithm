# 바둑판에 흰 돌 놓기

# 값 입력 받기
n = int(input())    # 흰 돌의 개수
my_list = []        # 흰 돌이 놓일 좌표 리스트 생성
for i in range(0, n):
    my_list.append(input().split())

# 바둑판 생성
rows, cols = (19, 19)
board = [[0 for i in range(cols)] for j in range(rows)]

# 흰 돌의 자리는 1로 대치
for j in range(0, n):
    row = int(my_list[j][0]) - 1
    column = int(my_list[j][1]) - 1
    board[row][column] = 1

for x in range(0, 19):
    for y in range(0, 19):
        print(board[x][y], end = ' ')
    print()
