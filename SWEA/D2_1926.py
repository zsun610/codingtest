n = int(input())
arr = []
for i in range(1,n+1):
    cnt = 0
    for j in str(i):
        if j == '3' or j == '6' or j == '9':
            cnt += 1
    if cnt > 0:
        arr.append('-'*cnt)
    else:
        arr.append(i)

for a in arr:
    print(a,end=' ')