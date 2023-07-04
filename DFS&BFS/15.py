# BFS
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n,m,k,x = map(int,input().split())

# 도로 정보 입력받기
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단거리 초기화
distance = [-1] * (n+1)
distance[x] = 0

# BFS
queue = deque([x])
while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[now]:
        if distance[next] == -1:   # 아직 방문하지 않은 도시라면
            distance[next] = distance[now] + 1  # 최단 거리 갱신
            queue.append(next)

check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)