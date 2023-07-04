result = eval("(3+5)*7")
print(result)

result2 = sorted([9,1,8,5,4], reverse=True)
print(result2)

result3 = sorted([('홍길동',35),('이순신',75),('아무개',50)], key = lambda x: x[1],reverse = True)

# permutations(리스트명,개수) - 순열(순서O) : iterable 객체에서 r개의 데이터를 뽑아 순서 있이 나열하는 경우의 수
from itertools import permutations
data = ['A','B','C']
presult = list(permutations(data,3)) # 3개를 뽑아 모든 순열 구하기
print(presult)   # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations(리스트명,개수) - 조합(순서X): iterable 객체에서 r개의 데이터를 뽑아 순서 없이 나열하는 경우의 수
from itertools import combinations
cresult = list(combinations(data,2))  # 3개를 뽑아 모든 조합 구하기
print(cresult)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# product(리스트명, : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수 (중복 O)
# product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import product
presult = list(product(data,repeat=2))   # 리스트 ['A','B','C']에서 중복을 포함하여 2개(r=2)를 뽑는 모든 순열 구하기(중복 허용)
print(presult)

# combinations_with_replacement : combinations와 같이 list와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) (중복 X)
from itertools import combinations_with_replacement
rresult = list(combinations_with_replacement(data,2))
print(rresult)
