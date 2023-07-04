from collections import deque

T = int(input())

for tc in range(1,T+1):
    n,m,k = map(int,input().split())
    people = list(map(int,input().split()))
    people.sort()

    cnt = 0
    z = 0
    for j in range(1,people[-1]+1):
        if j % m == 0:
            cnt += k
        if j == people[z]:
            if cnt > 0:
                cnt -= 1
                z += 1
            else:
                answer = 'Impossible'
                break

    if z == n:
        answer = 'Possible'
    print(f'#{tc} {answer}')
