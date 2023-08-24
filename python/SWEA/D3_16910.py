T = int(input())

for tc in range(1,T+1):
    n = int(input())
    result = 0
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            if i*i + j*j <= n*n:
                result += 1
    print(f'#{tc} {result}')