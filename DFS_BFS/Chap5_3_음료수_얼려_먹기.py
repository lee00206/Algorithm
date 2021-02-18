# 음료수 얼려 먹기
# 얼음 틀의 세로 길이 n과 가로 길이 m 입력받기
n, m = map(int, input().split())

# 얼음 틀의 형태 입력받기
array = []
for i in range(n):
    array.append(list(map(input().split())))


# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 범위를 벗어난 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드 방문
    if array[x][y] == 0:
        array[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출하여 방문
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대해 음료수 채우기
result = 0

for j in range(n):
    for k in range(m):
        if dfs(j, k) == True:
            result += 1

print(result)
