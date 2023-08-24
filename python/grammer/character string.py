# 큰 or 작은 따옴표 출력하고 싶을 때 밖에 다른 따옴표 입력하고 출력하고 싶은 따옴표 안에 넣기
data = "'Hello World'"
print(data)    # 'Hello World'
# \" + 문자열 + \"
data = "Don't you know \"Python\"?"
print(data)    # Don't you know "Python"?

a = "Hello"
b = "World"
print(a+" "+ b)   # Hello World
# 문자열에서도 인덱싱과 슬라이싱 사용 가능
c = "ABCDEF"
print(c[2:4])   # CD