# 틀렸음

n, k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()

# 바꾸는게 오히려 독일 수 있음, k번 안바꿀 수도
kcount = 0
for i in range(len(a)):
    a[i],b[len(b)-1-i] = b[len(b)-1-i],a[i]
    kcount += 1
    if kcount == k:
        break
# sum(a)
result = 0
for i in a:
    result += i
print(result)