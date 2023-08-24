for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())  # 행렬의 크기 3~50
    arr = [list(input()) for _ in range(n)]
    mymin = n * m

    # 1 for문으로 경우 전부 계산
    # 화이트
    for w in range(0, n - 2):
        white_cnt = m - arr[w].count('W')

        blue_cnt = 0   # 블루
        for b in range(w + 1, n - 1):
            blue_cnt = m - arr[b].count('B')

            red_cnt = 0  # 레드
            for r in range(b + 1, n):
                red_cnt = m - arr[r].count('R')

            cnt = white_cnt + blue_cnt + red_cnt
            if mymin > cnt:
                mymin = cnt

    print(f'#{tc} {mymin}')
