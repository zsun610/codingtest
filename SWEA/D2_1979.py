T = int(input())
for tc in range(1,T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        for j in range(n):
            # 행 탐색
            if arr[i][j] == 1:
                cnt1 += 1
            if arr[i][j] == 0 or j == n-1:
                if cnt1 == k:
                    result += 1
                cnt1 = 0
            # 열 탐색
            if arr[j][i] == 1:
                cnt2 += 1
            if arr[j][i] == 0 or j == n-1:
                if cnt2 == k:
                    result += 1
                cnt2 = 0
    print('#'+str(tc)+' '+str(result))