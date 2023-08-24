'''
8X8 체스판
경우의 수 1 : 맨 왼쪽 위 칸이 흰색인 경우
경우의 수 2: 맨 왼쪽 위칸이 검은색인 경우

sol)
if n,m == 8,8 이면 조건에 안맞는거 골라내기
if 8 < n,m < 50 이면 제일 적은거 찾아내기 - 완전 탐색으로
(왼쪽부터, 위부터)
'''

n,m = map(int,input().split())
array = [list(map(str,input())) for _ in range(n)]

def func1(array):
    chessboard1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    answer = 0
    for i in range(8):
        for j in range(8):
            if array[i][j] != chessboard1[i][j]:
                answer += 1
    return answer

def func2(array):
    chessboard2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
    answer = 0
    for i in range(8):
        for j in range(8):
            if array[i][j] != chessboard2[i][j]:
                answer += 1
    return answer

if n == 8 and m == 8:
    print(min(func1(array),func2(array)))

else:
    tmp = []
    for i in range(n - 8 + 1):
        for j in range(m - 8 + 1):
            # 배열 슬라이싱: 행을 먼저 자르고 그거에 대해 열도 자름
            part = [row[j:j + 8] for row in array[i:i + 8]]
            tmp.append(min(func1(part),func2(part)))
    print(min(tmp))