# 0일 때 각 칸마다 가장 가까운 상어로부터의 최대 안전거리를 구함
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0,-1,-1,1,1]
dy = [0,-1,0,1,-1,1,-1,1]

def bfs(now_x,now_y):
    queue = deque([(now_x,now_y)])
    dist = [[-1]*m for _ in range(n)]   # 최단거리 기록하는 맵
    dist[now_x][now_y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx,ny 가 graph 범위 내에 있고 아직 최단거리 업뎃이 안됐을 때
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
                # 거리 카운트
                if graph[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))
                else:   # graph[nx][ny] == 1일 때, 상어 마주침
                    result = dist[x][y] + 1
                    return result

answer = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer[i][j] = bfs(i,j)

max_value = 0
for i in range(n):
    for j in range(m):
        if answer[i][j] > max_value:
            max_value = answer[i][j]
print(max_value)



