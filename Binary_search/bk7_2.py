num1 = int(input())
arr1 = list(map(int,input().split()))
num2 = int(input())
arr2 = list(map(int,input().split()))

result = []
cnt = 0
for j in range(len(arr2)):
    for i in range(len(arr1)):
        cnt += 1
        if cnt == len(arr1):
            result.append("no")
        if arr2[j] == arr1[i]:
            result.append("yes")
            break

for i in range(len(result)):
    print(result[i], end = ' ')