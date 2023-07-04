# BFS
from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def func(x,y):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 or arr[nx][ny] == 1:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = 1
                queue.append((nx,ny))


result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result += 1
            func(i,j)
print(result)
