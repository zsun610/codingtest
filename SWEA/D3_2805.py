T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input())) for _ in range(n)]
    result = 0
    cnt = 0
    for i in range(n):
        k = cnt
        for j in range(n//2-k,(n//2)+k+1):
            result += arr[i][j]
        if i < n//2:
            cnt += 1
        else:
            cnt -= 1
    print(f'#{tc} {result}')