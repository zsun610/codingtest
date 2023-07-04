def dfs(number,x,y):
    if len(number) == 7:
        result.add(number)     # set 추가,제거 add, remove
        return
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(number + arr[nx][ny],nx,ny)

T = int(input())
for tc in range(1,T+1):
    arr = []
    for _ in range(4):
        arr.append(list(input().split()))
    result = set()
    for i in range(4):
        for j in range(4):
            dfs('',i,j)
    print('#{} {}'.format(tc,len(result)))
