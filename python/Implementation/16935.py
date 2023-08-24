def sol1(array,n,m):
    tmp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = array[n-1-i][j]
    return tmp

def sol2(array,n,m):
    tmp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tmp[i][j] = array[i][m-1-j]
    return tmp

def sol3(array,n,m):
    tmp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            tmp[i][j] = array[n-1-j][i]
    return tmp

def sol4(array,n,m):
    tmp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            tmp[i][j] = array[j][m-1-i]
    return tmp

def sol5(array,n,m):
    #1 = array[0:n/2+1][0:m/2+1]
    #2 = array[n/2+1:][0:m/2+1]
    #3 = array[n / 2 + 1:][m / 2 + 1:]
    #4 = array[0:n/2+1][m/2+1:]

    # for랑 if문 합쳐서 표현 가능
    tmp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i < n/2:
                if j < m/2:  #1
                    tmp[i][j] = array[i+n//2][j]
                else:  #2
                    tmp[i][j] = array[i][j-m//2]
            else:
                if j >= m/2:  #3
                    tmp[i][j] = array[i - n // 2][j]
                else:      #4
                    tmp[i][j] = array[i][j + m // 2]
    return tmp

def sol6(array,n,m):
    tmp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i < n/2:
                if j < m/2:  #1
                    tmp[i][j] = array[i][j+m//2]
                else:  #2
                    tmp[i][j] = array[i+n//2][j]
            else:
                if j >= m/2:  #3
                    tmp[i][j] = array[i][j-m//2]
                else:    #4
                    tmp[i][j] = array[i-n//2][j]
    return tmp


n,m,r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
order = list(map(int,input().split()))

for i in order:
    if i == 1:
        arr = sol1(arr,n,m)
    if i == 2:
        arr = sol2(arr,n,m)
    if i == 3:
        arr = sol3(arr,n,m)
        n,m = m,n
    if i == 4:
        arr = sol4(arr,n,m)
        n,m = m,n
    if i == 5:
        arr = sol5(arr,n,m)
    if i == 6:
        arr = sol6(arr,n,m)

for a in arr:
    print(*a)