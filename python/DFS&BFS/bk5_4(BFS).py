from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input())) for _ in range(n)]

queue = deque()
queue.append((0,0))
# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 or arr[nx][ny] == 0:
            continue
        if arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            queue.append((nx,ny))
        if nx == n-1 and ny == m-1:
            break
print(arr[n-1][m-1])