def func(arr,row_start,col_start,n):
    global blues
    global whites

    blue_cnt = 0
    white_cnt = 0
    for i in range(row_start,row_start+n):
        for j in range(col_start,col_start+n):
            if arr[i][j] == 1:
                blue_cnt += 1
            else:
                white_cnt += 1

    if blue_cnt == n*n:
        blues += 1
    elif white_cnt == n*n:
        whites += 1
    elif n == 1:
        return True
    else:
        func(arr, row_start, col_start, n//2)
        func(arr, row_start + n//2, col_start, n//2)
        func(arr, row_start, col_start + n//2, n//2)
        func(arr, row_start + n//2, col_start + n//2, n // 2)


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    blues = 0
    whites = 0

    func(arr,0,0,n)

    print('#{} {} {}'.format(tc,whites,blues))