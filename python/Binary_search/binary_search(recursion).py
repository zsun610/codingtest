# 이진 탐색 코드 (재귀 함수) : target 과 같은 값을 array에서 찾아 순위 반환
def binary_search(array,target,start,end):
    if start > end:
        return None
    # 중간점
    mid = (start+end)//2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] < target:   # 중간값보다 작은 경우
        return binary_search(array, target, start, mid - 1)
    else:                       # 중간값보다 큰 경우
        return binary_search(array, target, mid + 1, end)

n, target = map(int,input().split())
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)