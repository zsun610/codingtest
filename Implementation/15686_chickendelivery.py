from itertools import combinations
INF = 1e9
# 0: 빈 칸, 1: 집, 2: 치킨 집
n,m = map(int,input().split())  # n: nxn 도시, m: 치킨 집 개수
graph = [list(map(int,input().split())) for _ in range(n)]

# 집과 치킨 집 좌표를 담는 리스트 생성
home,chicken = [],[]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:    # 집일 때 좌표 home에 저장
            home.append((i,j))
        elif graph[i][j] == 2:  # 치킨 집일 때 좌표 chicken에 저장
            chicken.append((i, j))

# chicken 리스트에서 m개의 치킨집을 뽑는 조합 생성
nCm = list(combinations(chicken,m))

def get_sum(candidate):
    sum_dist = 0   # 치킨거리의 합
    # 각 집마다 최소 치킨 거리 구함
    for hx,hy in home:
        tmp_dist = INF  # 집 바뀔때마다 거리 초기화
        for cx,cy in chicken:
            # 현재 집에서 제일 가까운 치킨집까지와의 거리 구하기
            tmp_dist = min(tmp_dist,abs(hx-cx) + abs(hy-cy))
        sum_dist  += tmp_dist     # 각 집마다 제일 가까운 치킨집과의 거리 합하기
    return sum_dist

# 조합리스트에서 각 치킨집 조합에 대해 치킨거리합 계산
answer = INF
for candidate in nCm:
    # 조합들 중 치킨거리가 가장 작은 값을 결과로 도출
    answer = min(answer,get_sum(candidate))

print(answer)
