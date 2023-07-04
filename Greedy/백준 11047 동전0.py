import time

start_time = time.time()

N, K = map(int, input.split())
arr = []
for _ in range(1,N+1):
    Ai = input()
    if Ai < K:
        arr.append(Ai)
cnt = 0
tmp = 0
for i in range(len(arr)-1):
    while tmp < K:
        tmp = tmp + arr[i]
        cnt = cnt + 1
    if tmp == K:
        break

end_time = time.time()

print("time :", end_time - start_time)