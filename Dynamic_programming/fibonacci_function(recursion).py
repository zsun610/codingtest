# 피보나치 수열 - 재귀, Top-down, memoization

# 한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화, fibo(99) 100개 항
d = [0] * 100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이내믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


d2 = [0]*100

def pibo(x):
    print('f('+str(x)+')',end=' ')
    if x == 1 or x == 2:
        return 1
    if d2[x] != 0:
        return d2[x]
    d2[x] = pibo(x-1) + pibo(x-2)
    return d2[x]

pibo(6)