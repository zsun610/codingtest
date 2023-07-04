# 입력
# 입력 개수가 많은 경우
import sys
data = sys.stdin.readline().rstrip() # 문자열 입력받기
print(type(data))

# 공백을 구분으로 n,m,k 3개 데이터 입력받음
n, m, k = map(int,input().split())
print(n,m,k)
# 각 데이터를 공백으로 구분하여 입력 (map 유형은 출력이 안되기에 list로 변환)
data2 = list(map(int, input().split()))

# 문자열과 숫자를 함께 출력할 때
# 1. 숫자를 문자열로 바꿔줌, str() 과 + 사용, + -> 띄어쓰기 생성X
answer = 7
print("정답은 "+str(answer)+"입니다.")   # 정답은 7입니다.
# 2. 각 자료형을 콤마(,)로 구분함 ( , -> 띄어쓰기 생성)
print("정답은",answer,"입니다.")    # 정답은 7 입니다.
# 3. f-string 사용 : 문자열 앞에 접두사 f 붙이고 {} 안에 변수를 넣음
print(f"정답은 {answer}입니다.")    # 정답은 7입니다.