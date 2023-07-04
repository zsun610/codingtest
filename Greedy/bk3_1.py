N = 1260
cnt = 0
array = [50, 100, 500, 10]
array.sort(reverse=True)

for i in array:
    cnt += N // i
    N %= i
print(cnt)
