# list, tuple 순서O -> 인덱싱으로 자료형의 값을 얻을 수 있음

# tuple: 튜플은 한 번 선언된 값을 변경할 수 없다.
t = (1,2,3,4)

# list
x = 10
a = [0] * x # [0,0,0,0,0,0,0,0,0,0]

b = [1,2,3,4,5,6,7,8,9]
print(b[-1])  # 뒤에서 첫번째 원소 출력 9
print(b[-3])  # 뒤에서 세번째 원소 출력 7
print(b[1:4]) # 마지막 인덱스 포함X [2,3,4]

b.append(3)   # 리스트에 원소를 하나 삽입할 때 사용
b.sort()      # 오름차순 정렬
b.sort(reverse=True) # 내림차순 정렬
b.reverse     # 원소 순서를 뒤집기
b.insert(2,0) # 리스트명.insert(인덱스,삽입할 값)
b.count(3)    # 특정 값의 개수를 세어줌
b.remove(3)   # 특정 값을 제거, 여러개면 하나만 제거

c = [1,2,3,4,5,5,5]
remove_set = {3,5}
# remove_set에 포함되지 않은 값만 저장
result = [i for i in c if i not in remove_set]

# list comprehension
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
arr = [i for i in range(20) if i % 2 == 1]

# N X M 2차원 리스트 초기화 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
n = 3
m = 4
array = [[0] * m for _ in range(n)]

