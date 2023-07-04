n, m = map(int,input().split())
x, y, d = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

# 북,동,남,서
d_order = [0,3,2,1]

# U,R,D,L
dx = [-1,0,1,0]
dy = [0,-1,0,1]

arr[x][y] = 2
cnt = 0
result = 0
while True:
    for i in range(len(d_order)):
        if cnt > 3:
            x = x - dx[i]
            y = y - dy[i]
            cnt = 0
            if arr[x][y] == 1:
                break
        elif (x + dx[i]) >= 1 and (x + dx[i]) <= (n - 2) and (y + dy[i]) >= 1 and (y + dy[i]) <= (n - 2) and arr[x+dx[i]][y+dy[i]] == 0:
            x = x + dx[i]
            y = y + dy[i]
            arr[x][y] = 2
            result += 1
            cnt = 0
        else:
            cnt += 1
print(result)