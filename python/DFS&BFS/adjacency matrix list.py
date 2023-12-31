# 인접 행렬 방식 예시 - 2차원 리스트, 모든 정보를 저장
INF = 9999999999 # 무한의 비용 선언 (9자리)
# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
    ]
print(graph)

# 인접 리스트 방식 예시 - 2차원 리스트, 연결된 정보만 저장
# 빈 2차원 리스트 선언
graph2 = [[] for _ in range(3)]

# 각 노드에 연결된 노드 정보 '튜플'로 저장
# 인덱스:노드번호, 튜플:(연결노드, 거리) - 0이랑 INF 무시, 정보가 든 것만 저장
# 노드 0에 연결된 노드 정보 저장(연결노드, 거리)
graph2[0].append((1,7))
graph2[0].append((2,5))
# 노드 1에 연결된 노드 정보 저장(연결노드, 거리)
graph2[1].append((0,7))
# 노드 2에 연결된 노드 정보 저장(연결노드, 거리)
graph2[2].append((0,5))

print(graph2)   # [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]