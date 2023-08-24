# fibonacci 점화식: an = f(n-1,n-2) = an-1 + an-2
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))  # 3

# fibo(3) + fibo(2)   ( 2 + 1 )
# fibo(2) + fibo(1)   ( 1 + 1 )