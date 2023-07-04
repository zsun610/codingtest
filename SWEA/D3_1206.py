for tc in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    result = 0
    for i in range(2,n-2):
        max_num = max(arr[i-1],arr[i-2],arr[i+1],arr[i+2])
        if arr[i] > max_num:
            result += arr[i] - max_num
        else:
            continue
    print('#{} {}'.format(tc,result))