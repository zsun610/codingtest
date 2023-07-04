# 달팽이 문제

T = int(input())

for test_case in range(1,T+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]    # 파이썬 2차원 리스트 초기화
    x, y = 0,0         # 달팽이 시작 위치
    cnt = 1            # 첫번째 배열 값
    dr = 0             # 방향 값
    arr[x][y] = 1      # 첫번째 값
    # 달팽이 방향 전환 순서 R->D->L->U
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    # cnt가 n*n일때까지 수행함
    while cnt < n*n:
        nx = x + dx[dr]
        ny = y + dy[dr]
        # nx와 ny가 범위 내이면서 아직 값이 채워지지 않은 상태일 때 값을 채워줌
        if nx >= 0 and nx <= n-1 and ny >= 0 and ny <= n-1 and arr[nx][ny] == 0:
            cnt += 1
            x = nx
            y = ny
            arr[x][y] = cnt
        # nx,ny가 범위를 벗어났거나 이미 값이 채워진 상태일 때 방향전환
        else:
            dr = (dr + 1) % 4
    
    # 테케 번호 출력
    print('#'+ str(test_case))
    # 배열 출력
    for i in arr:
        print(*i)