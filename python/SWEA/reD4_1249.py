from collections import deque

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    graph = [list(map(int,input())) for _ in range(n)]

    queue = deque()
    queue.append((0,0))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[False] * n for _ in range(n)]

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    graph[nx][ny] += graph[x][y]
                    visited[nx][ny] = True
                else:   # 만약 이미 방문했다면
                    if graph[nx][ny] > graph[nx][ny] + graph[x][y]:
                        queue.append((nx, ny))
                        graph[nx][ny] += graph[x][y]

    print(graph[n-1][n-1])

