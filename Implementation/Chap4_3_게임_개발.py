# 게임 개발
# 맵의 크기 입력받기
n, m = map(int, input().split())

# 좌표, 방향 입력받기
point_x, point_y, direction = map(int, input().split())
x = point_x
y = point_y

# 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 왼쪽 회전
def turn_left():
    global direction
    if direction != 0:
        direction -= 1
    else:
        direction = 3

# 회전 횟수 세기
turn_direction = 0

# 북쪽을 향해있는 경우
def north():
    global x, y, array, turn_direction
    if array[x - 1][y] == 0:
        array[x - 1][y] = 9
        x = x - 1
        turn_direction = 0
    else:
        turn_left()
        turn_direction += 1

# 동쪽을 향해있는 경우
def east():
    global x, y, array, turn_direction
    if array[x][y + 1] == 0:
        array[x][y + 1] = 9
        y = y + 1
        turn_direction = 0
    else:
        turn_left()
        turn_direction += 1

# 남쪽을 향해있는 경우
def south():
    global x, y, array, turn_direction
    if array[x + 1][y] == 0:
        array[x + 1][y] = 9
        x = x + 1
        turn_direction = 0
    else:
        turn_left()
        turn_direction += 1

# 서쪽을 향해있는 경우
def west():
    global x, y, array, turn_direction
    if array[x][y - 1] == 0:
        array[x][y - 1] = 9
        y = y - 1
        turn_direction = 0
    else:
        turn_left()
        turn_direction += 1

# 시뮬레이션
array[x][y] = 9

while True:
    # 왼쪽으로 회전
    turn_left()

    if direction == 0 and turn_direction < 4:
        north()
    elif direction == 1 and turn_direction < 4:
        east()
    elif direction == 2 and turn_direction < 4:
        south()
    elif direction == 3 and turn_direction < 4:
        west()
    # 네 방향 모두 갈 수 없는 경우
    else:
        # 뒤로 갈 수 있다면 이동
        if array[x][y] != 1 and direction == 0:
            x += 1
        elif array[x][y] != 1 and direction == 1:
            y -= 1
        elif array[x][y] != 1 and direction == 2:
            x -= 1
        elif array[x][y] != 1 and direction == 3:
            y += 1
        else:
            break

# 가본 칸 세기
count = 0

for j in range(n):
    for k in range(m):
        if array[j][k] == 9:
            count += 1

print(count)
