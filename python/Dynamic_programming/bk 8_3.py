n = int(input())
d = list(map(int,input().split()))

arr = [0]*101
cnt = 0
for i in range(1,n):
    if i == n-1 and d[i-1] < d[i] and arr[i] == 0:
        cnt += d[i]
    elif d[i-1] <= d[i] <= d[i+1] and arr[i] == 0:
        cnt += d[i]
        arr[i-1] = 1
        arr[i] = 1
        arr[i+1] = 1

print(cnt)