# 구현 문제 길수록 함수를 나누는 것 생각하기, 무엇을 입력인자, 출력인자로 할지
# 함수1(BFS): 최단거리를 저장하는 맵 만들기
# 함수2: 최단거리 맵을 통해 가장 가까운 물고기 찾아먹기
'''
1. 맵 입력 받기
2. 아기상어 현재 좌표, 현재 크기 설정
3. 현재 위치에서 갈 수 있는 최단거리 구하는 함수 >> bfs
4. 아기상어가 먹는 물고기 구하는 함수
5. 시행
'''

from collections import deque
INF = 1e9

# 맵 정보 입력받기
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

now_size = 2        # 아기상어 크기
now_x,now_y = 0,0   # 아기상어 좌표

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x,now_y = i,j
            graph[i][j] = 0
            break

# 상,좌,하,우 (U,L,D,R)
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 모든 위치까지의 최단거리만 계산하는 BFS
def bfs():
    #값이 -1이라면 도달할 수 없음(초기화)
    dist = [[-1]*n for _ in range(n)]

    # 시작 위치는 도달 가능하며 거리는 0
    queue = deque([(now_x,now_y)])
    dist[now_x][now_y] = 0

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx,ny))
    # 모든 위치까지의 최단거리 테이블 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 현위치에서 최단거리 물고기를 찾는 함수
def find(dist):
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and graph[i][j] >= 1 and graph[i][j] < now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x,y = i,j
                    min_dist = dist[i][j]
    # 먹을 수 있는 물고기가 없는 경우
    if min_dist == INF:
        return None
    else:
        return x,y,min_dist

result = 0    # 몇 초 동안 엄마상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지
ate = 0       # 아기상어가 현재 크기에서 물고기 먹은 개수

while True:
    #먹을 수 있는 물고기 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x,now_y = value[0],value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        graph[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0