# 레이저 만나면 레이저 왼쪽 '(' 의 개수를 세줌 = 잘린 막대기 개수
# ')' 만나면 결과 += 1 ( 끝점 겹치는 건 없기 때문)
# 이 방법으로 풀려면 로직 잘짜야
T = int(input())
for tc in range(1, T+1):
    input_data = list(input())
    stack = []
    result = 0
    for i in range(len(input_data)):
        if input_data[i] == '(':
            stack.append('(')
        else:  # input_data[i] == ")" 면
            stack.pop()
            if input_data[i-1] == '(':
                result += len(stack)
            else:
                result += 1
    print(f'#{tc} {result}')