num = int(input())

arr=[]
for i in range(num):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i, end = ' ')