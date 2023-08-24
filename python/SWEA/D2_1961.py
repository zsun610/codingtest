T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    arr90 = [[0]*n for _ in range(n)]
    arr180 = [[0]*n for _ in range(n)]
    arr270 = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 배열 접근할 때 왼쪽 원소를 arr[n-1-j][i] 이런식으로 접근하면 안됨
            arr90[i][j] = arr[n-1-j][i]
            arr180[i][j] = arr[n-1-i][n-1-j]
            arr270[i][j] = arr[j][n-1-i]

    print('#'+str(tc))
    for i in range(n):
        for a in range(n):
            print(arr90[i][a],end='')
        print(end = ' ')
        for b in range(n):
            print(arr180[i][b],end='')
        print(end = ' ')
        for c in range(n):
            print(arr270[i][c],end='')
        print()