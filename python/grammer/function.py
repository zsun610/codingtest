# def 함수명(매개변수): ~ return 반환값
# 매개변수, 반환값 없을 수 있음

# 매개변수 지정 가능
def add(a,b):
    print('함수의 결과:',a+b)
add(b=3,a=7)

# global
a = 0
def func():
    global a
    a += 1
for i in range(10):
    func()
print(a) # 10