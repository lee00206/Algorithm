# 전보 - 개선된 다익스트라 알고리즘 사용
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 n과 통로의 개수 m, 메세지를 보내고자 하는 도시 c 입력받기
n, m, c = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담은 리스트
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    # x에서 y로 가는 시간이 z
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:    # q가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

# 도달할 수 있는 도시의 수
count = 0

# 가장 멀리 있는 도시까지의 거리
max_distance = 0

for i in range(distance):
    if distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])

print(count - 1, max_distance)