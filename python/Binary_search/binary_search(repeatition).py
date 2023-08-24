# 이진 탐색 코드 (반복문) : target 과 같은 값을 array에서 찾아 순위 반환
# 이진 탐색에선 주로 입력값이 많아 import sys 사용
import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start+end)//2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid -1
        else:
            start = mid + 1

n, target = map(int,input().split())
array = list(map(int,input().split()))

result = (array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)