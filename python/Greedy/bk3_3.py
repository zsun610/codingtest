N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    data.sort()
    if data[0] > result:
        result = data[0]

print(result)