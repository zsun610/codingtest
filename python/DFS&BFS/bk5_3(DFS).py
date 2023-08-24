# 함수 사용, DFS, 코드 그냥 암기 (연결된 덩어리 찾기)

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1    # 해당 노드 방문 처리
        # 상,하,좌,우 덩어리 찾기
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)