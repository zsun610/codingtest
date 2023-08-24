T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    max_line = max(n,m)
    min_line = min(n,m)

    if n >= m:
        max_arr = arr1
        min_arr = arr2
    else:
        max_arr = arr2
        min_arr = arr1

    results = []
    for i in range(max_line-min_line+1):
        cnt = 0
        for j in range(min_line):
            cnt += min_arr[j]*max_arr[i+j]
        results.append(cnt)

    print('#'+str(tc)+' '+str(max(results)))

