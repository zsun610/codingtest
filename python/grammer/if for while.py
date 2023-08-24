# 조건문 if, elif, else
# 비교 연산자 : ==, !=, >, <, >=, <=
# 논리 연산자 : and, or, not x ( x가 거짓(False)일 때 참(True))

# pass : 조건문이 참이더라도 아무것도 처리하고 싶지 않을 때 사용
score = 85
if score >= 80:
    pass # 나중에 작성할 코드
else:
    print('성적이 80점 미만입니다.')
print('프로그램을 종료합니다.')

# 반복문 for, while
# for ~ in ~ 뒤에 오는 데이터 : list, tuple, 문자열
# for - continue : 해당 인덱스 처리 안하고 다음 인덱스로 ( for문으로 돌아감)
# continue와 pass의 차이 : continue는 반복문의 다음 인덱스로 넘어가지만 (i+1) pass는 다음 문장으로 넘어감

scores = [90,85,77,65,97]
cheating_list = {2,4}

for i in range(5):
    if i + 1 in cheating_list:
        continue
    if scores[i] >= 80:
        print(i+1,"합격입니다.")