num1 = int(input())
arr1 = list(map(int,input().split()))
num2 = int(input())
arr2 = list(map(int,input().split()))

arr1.sort()
arr2.sort()

def binary_search(array,target,start,end):
    mid = (start + end)//2
    while start <= end:
        if array[mid] == target:
            return 'yes'
        elif array[mid] < target:
            return binary_search(array,target,mid+1,end)
        else:
            return binary_search(array,target,start,mid-1)
    return 'no'

result = []
for i in arr2:
    result.append(binary_search(arr1,i,0,num1-1))

print(result)