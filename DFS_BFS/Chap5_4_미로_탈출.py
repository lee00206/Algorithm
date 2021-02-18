# 미로 탈출
from collections import deque

# 행열 입력받기
n, m = map(int, input().split())

# 미로 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 상하좌우 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))    # 현재 좌표

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]      # 다음 x 좌표
            ny = y + dy[i]      # 다음 y 좌표
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 부분 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))