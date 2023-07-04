# dictionary, set 순서X -> 인덱싱 불가
# dictionary : key - value 쌍을 데이터로 가짐 (순서x - 순서 지정하고 싶다면 lamda 사용해서 key 조건을 추가)
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

if '사과' in data:
    print("있음")
# 리스트명.keys() : 키값만 뽑아 리스트 생성 / 리스트명.values() : 값만 뽑아 리스트 생성

x = {"a":10, "b":20}
print(len(x))  # 2
print(x["a"])  # 10
x["a"] = 30    # {"a":30, "b":20}
x["c"] = 40    # {"a":30, "b":20, "c":40}
del x["b"]     # {"a":30, "c":40}

# 딕셔너리 자료에 특정 키가 있는지 없는지 알기 위해선 in 활용
print("a" in x)    # True
print("d" in x)    # False

# 딕셔너리 반복문 : 1. 키만 반복 2. 값만 반복 3. 키와 값 쌍을 반복
# 1. 키만 반복
for k in x:
    print(k)    # a ,c

for k in x.keys():
    print(k)    # a ,c

# 2. 값만 반복
for v in x.values():
    print(v)    # 30,40

#3. 키와 값 쌍을 반복
for k,v in x.items():
    print("key [%s] => value [%d]" % (k,v))
    #key [a] => value [30]
    #key [c] => value [40]

# set : 리스트나 문자열을 이용해 만듦, 중복X, 순서X, 키X(값만)
# >> 특정한 데이터가 이미 등장한 적이 있는지 여부 체크
data2 = set([1,1,2,3,4,4,5])
data3 = {1,1,2,3,4,4,5}
print(data2)
print(data3)
# 합집합(|), 교집합(&), 차집합(-) 사용가능
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a|b)
print(a&b)
print(a-b)