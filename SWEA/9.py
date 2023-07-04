T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split())
    rows = []
    columns = []
    for i in range(1, N + 1):
        a, b = map(int, input().split())
        rows.append(a)
        columns.append(b)

    R = max(rows) - 1
    tmp1 = M - min(columns)
    tmp2 = max(columns) - 1
    C = min(tmp1, tmp2)

    print("#" + str(tc) + " " + str(R + C))