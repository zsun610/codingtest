from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# R,D
dx = [0,1]
dy = [1,0]
visited = [[False] * n for _ in range(n)]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        move = graph[x][y]
        if move == -1:
            return True
        for i in range(2):
            nx = x + (dx[i] * move)
            ny = y + (dy[i] * move)

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                queue.append((nx, ny))

if bfs(0,0):
    print("HaruHaru")
else:
    print("Hing")