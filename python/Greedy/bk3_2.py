N, M, K = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력
data = list(map(int, input().split()))
data.sort()

cnt = 0
first = data[-1]
second = data[-2]

if M < K:
    cnt = first * M
else:
    first_num = first * (M - (M % K))
    second_num = second * (M % K)
    cnt = first_num + second_num
print(cnt)