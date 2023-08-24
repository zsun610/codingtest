array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right <= end and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot],array[right]
        else:
            array[left],array[right] = array[right], array[left]
        quick_sort(array,start,right-1)
        quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)