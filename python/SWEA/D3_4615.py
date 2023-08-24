T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())

    graph = [[0]*(n+1) for _ in range(n+1)]
    graph[n//2][n//2] = 2
    graph[(n // 2)+1][n // 2] = 1
    graph[n // 2][(n // 2) + 1] = 1
    graph[(n // 2)+1 ][(n // 2)+1] = 2

    for i in range(m):
        x,y,color = map(int,input().split())
        graph[x][y] = color

        dx = [-1,1,0,0,-1,-1,1,1]
        dy = [0,0,-1,1,-1,1,-1,1]
        r = []
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1 <= nx <= n and 1 <= ny <= n:
                if graph[nx][ny] == 0:
                    break
                elif graph[nx][ny] == color:
                    while r:
                        nnx,nny = r.pop()
                        graph[nnx][nny] = color
                else:
                    r.append((nx,ny))
            else:
                break

    whites, blacks = 0,0
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] == 1:
                blacks += 1
            elif graph[i][j] == 2:
                whites += 1
    print(f'#{tc} {blacks} {whites}')


