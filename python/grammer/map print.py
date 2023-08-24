def double(x):
    return x*2

numbers = [1,2,3,4,5]
result = map(double,numbers)

print(type(result))

N,M = map(int,input().split())
x,y,d = map(int,input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

print(arr)