x = int(input())

d = [0] * 30001

# Bottom-up
for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)   # d[i] : 뺴기 연산 ( 앞 작은 수 + 1) , d[i//2]+1 : 나누기에 연산 한 번(나눠떨어짐) 더 더함
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)
print(d[x])