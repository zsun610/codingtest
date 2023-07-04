T=int(input())

for tc in range(1,T+1):
    n = input()

    results = []
    for i in range(1, len(n)):
        results.append(int(n[:i])+int(n[i:]))
    print('#{} {}'.format(tc,min(results)))