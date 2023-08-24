'''
1. 입력값 받기
2. 물고기 번호 배열, 방향 배열 따로 생성한다.
3. 물고기 이동하는 함수
4. 상어 이동하는 함수
'''

graph = [list(map(int,input().split())) for _ in range(4)]

# 물고기 숫자 배열, 물고기 방향 배열 따로 저장하기
num = [[0] * 4 for _ in range(4)]
vector = [[0] * 4 for _ in range(4)]
for i in range(4):
    for j in range(8):
        if j % 2 == 0:
            num[i][j//2] = graph[i][j]
        else:
            vector[i][j//2] = graph[i][j]-1  # 1~8 -> 0~7

# 상어 초기 위치
shark_x,shark_y = 0,0
# 물고기 잡아 먹음
result = num[shark_x][shark_y]        # 결과에 물고기 숫자 더함
sharkvec = vector[shark_x][shark_y]   # 상어벡터
# 상어 초기위치 (0,0)에 88로 표현
num[shark_x][shark_y] = 88
vector[shark_x][shark_y] = 88

# 물고기 이동 순서 :상,좌상,좌,좌하,하,우하,우,우상 (0~7) (반시계 방향)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
def fish_move():
    fish_num = 0
    while fish_num <= 16:
        fish_num += 1
        now_x,now_y = 99,99  # 있는지 확인 위해 초기화
        for i in range(4):
            for j in range(4):
                if num[i][j] == fish_num:
                    now_x,now_y = i,j # 현재 물고기 좌표
        # 이미 먹힌 번호여서 없을 때는 다음 번호로
        if now_x == 99 and now_y == 99:
            continue

        nowvec = vector[now_x][now_y]  # 현재 물고기 벡터
        vec_change = 0  # 벡터 바꾼 횟수
        while vec_change < 8:
            # 현재 물고기 벡터 방향에 있는 물고기 좌표
            swap_x = now_x + dx[nowvec]
            swap_y = now_y + dy[nowvec]
            # 공간 내이면서 상어가 없는 칸일 때
            if 0 <= swap_x < 4 and 0 <= swap_y < 4 and num[swap_x][swap_y] != 88 and vector[swap_x][swap_y] != 88:
                # 현재 물고기와 벡터 방향에 있는 물고기를 swap
                num[now_x][now_y],num[swap_x][swap_y] = num[swap_x][swap_y],num[now_x][now_y]
                vector[now_x][now_y],vector[swap_x][swap_y] = vector[swap_x][swap_y],vector[now_x][now_y]
                break
            # 공간 밖이거나 상어가 있는 칸
            else:
                nowvec = (nowvec + 1) % 8   # 방향 바꿔준다.
                vec_change += 1


def shark_move(shark_x,shark_y,sharkvec):
    # 상어가 떠날 자리, 물고기 먹음 처리
    num[shark_x][shark_y] = 0
    vector[shark_x][shark_y] = 0

    tmp_x,tmp_y = shark_x,shark_y   # 상어 이동했는지 확인하기 위해
    # 상어가 이동할 수 있는 칸들 중 가장 큰 물고기가 있는 칸으로 이동
    max_num = 0
    while True:
        nx = shark_x + dx[sharkvec]
        ny = shark_y + dy[sharkvec]
        # 1. 범위 내  2. 물고기가 존재하는 칸
        if 0 <= nx < 4 and 0 <= ny < 4 and num[nx][ny] != 0 and vector[nx][ny] != 0:
            if max_num < num[nx][ny]:
                max_num = num[nx][ny]
                shark_x, shark_y = nx, ny
                sharkvec = vector[shark_x][shark_y]
        else:
            break

    if tmp_x == shark_x and tmp_y == shark_y:
        return False
    else:
        return shark_x,shark_y,sharkvec


while True:
    fish_move()
    value = shark_move(shark_x,shark_y,sharkvec)
    if value == False:
        break
    else:
        shark_x, shark_y, sharkvec = value[0], value[1], value[2]
        result += num[shark_x][shark_y]
        # 상어 위치 업데이트
        num[shark_x][shark_y] = 88
        vector[shark_x][shark_y] = 88

print(result)
