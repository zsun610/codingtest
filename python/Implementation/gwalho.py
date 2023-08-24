# 예외처리 잘해야..
# 1.괄호 짝 2.괄호순서
def solution(s):
    answer = 0
    for i in range(len(s)):
        new = s[i:] + s[:i]
        # 괄호순서
        tmp = []
        for j in range(len(new)):
            if new[j] == '(' or new[j] == '[' or new[j] == '{':
                correct = False
                tmp.append(new[j])
            elif new[j] == ')':
                if '(' in tmp and tmp[-1] == '(':
                    tmp.pop()
                    correct = True
                else:
                    correct = False
                    break

            elif new[j] == ']':
                if '[' in tmp and tmp[-1] == '[':
                    tmp.pop()
                    correct = True
                else:
                    correct = False
                    break
            elif new[j] == '}':
                if '{' in tmp and tmp[-1] == '{':
                    tmp.pop()
                    correct = True
                else:
                    correct = False
                    break

        if correct == True and tmp == []:
            answer += 1
    return answer