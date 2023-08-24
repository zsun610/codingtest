from collections import deque

n,m,k = map(int,input().split())
graph = [[0] * m for _ in range(n)]
territory = [list(map(int,input().split())) for _ in range(k)]
for i in range(k):
    # 행이 위아래 바뀌어 있기에 n - 로 거꾸로, 열은 그대로임
    for x in range(n-territory[i][3],n-territory[i][1]):
        for y in range(territory[i][0],territory[i][2]):
            graph[x][y] = 1

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    queue = deque([(x,y)])
    answer = 0
    while queue:
        x,y = queue.popleft()
        # 여기다가 하면 (x,y)가 중복으로 들어와 중첩될 수 있음
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 0 이어야만 숫자 업데이트
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx,ny))
                answer += 1
                graph[nx][ny] = answer

    # 카운팅이 안됐을 경우
    if answer == 0:
        answer += 1
    return answer

cnt = 0
result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
            result.append(bfs(i,j))
result.sort()
print(cnt)
print(*result)
