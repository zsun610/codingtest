n = int(input())
move = list(map(str,input().split()))

arr = [[0]*n for _ in range(n)]
x,y = 1,1

for i in move:
    if i == 'L' and y != 1:
        y -= 1
    if i == 'R' and y != n:
        y += 1
    if i == 'U' and x != 1:
        x -= 1
    if i == 'D' and x != n:
        x += 1

print(x,y)