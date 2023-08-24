n = int(input())  # N X N 정사각 보드
graph = [[0]*n for _ in range(n)]

k = int(input())  # 사과 개수
for _ in range(k):
    apple_x,apple_y = map(int, input().split()) # 사과 위치
    graph[apple_x - 1][apple_y - 1] = 'o'

l = int(input()) # 뱀 방향변환 횟수
arr = []
for _ in range(l):
    # t초 후 c ('L':왼쪽 or 'D':오른쪽 으로 90도 회전)
    a,b = input().split()
    arr.append([a,b])

arr.append([150,"L"])  # 마지막 방향전환 이동시키기 위해 추가

# 우,하,좌,상
dx = [0,1,0,-1]
dy = [1,0,-1,0]
d = 0                  # 방향 index

x,y = 0,0              # 뱀 초기 위치
graph[x][y] = 1        # 그래프에 뱀을 1로 표현
snake_move = [(0,0)]   # 뱀 경로 저장
t_cnt = 0              # 게임 끝나기까지 걸린 시간
crash = 0              # 몸과 충돌

for i in range(l+1):
    t = int(arr[i][0])   # 초
    c = arr[i][1]        # 방향

    if x < 0 or x >= n or y < 0 or y >= n or crash == 1:
        break

    while t_cnt < t:

        t_cnt += 1  # 시간 카운트
        # 뱀 움직임
        x += dx[d]
        y += dy[d]

        # 벽에 부딪히거나 자신의 몸에 부딪히면 종료
        if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 1:
            crash = 1
            break

        # 사과 X >> 꼬리 제거
        elif graph[x][y] == 0:
            tail_x = snake_move[0][0]
            tail_y = snake_move[0][1]
            graph[tail_x][tail_y] = 0    # 꼬리 칸을 비워줌
            snake_move = snake_move[1:]  # 움직임에 update

        snake_move.append((x,y))  # 몸 길이 + 1
        graph[x][y] = 1 # 뱀 머리 ㅍ ㅍ  ㅠ 이동


    # 방향전환
    if c == 'L':
        d -= 1
        if d < 0:
            d += 4
    else:
        d += 1
        if d > 3:
            d %= 4

print(t_cnt)
