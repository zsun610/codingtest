
n = int(input())
array = set(map(int,input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:   # 집합 사용
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
