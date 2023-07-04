'''
hanoi(5,1,3,2)
5개의 기둥을 1번 시작기둥에서 3번 목표기둥으로 2번 기둥을 보조로 사용

def hanoi(원반개수,시작,목표,보조):
    # 원반 개수가 1개라면 바로 시작 -> 목표기둥으로 옮기고 종료
    if 원반개수 == 1:
        print(시작, '->', 목표)
        return
    # 원반 개수가 2개이상이라면 가장 큰 원반을 제외한 모든 원반은 보조 기둥으로, 가장 큰 원반은 목표기둥으로
    >> 맨 아래(가장 큰) 원반을 제외하고 모두 보조기둥으로 이동
    hanoi(원반개수 -1, 시작,보조,목표)
    print(시작, '->', 목표)
    # 가장 큰 원반을 목표기둥으로 옮겼기에 기둥을 1개를 제외하고 이동 (원반 개수 n -1 개, 원반 모두 보조기둥에)
    hanoi(원반개수 -1, 보조,목표,시작)
'''

def hanoi(num,start,end,assist):
    # 가장 큰 원반을 시작 기둥에서 목표 기둥으로 옮김
    if num == 1:
        print(start, '->', end)
        return
    # 가장 큰 원반을 제외하고 나머지 원반들을 보조기둥으로 옮김
    hanoi(num -1, start, assist, end)
    print(start, '->', end)
    # 보조 기둥에서 목표기둥으로 다 옮김
    hanoi(num -1,assist,end,start)

def hanoi(num,start,end,assist):
    # 가장 큰 원반을 시작 기둥에서 목표 기둥으로 옮김
    if num == 1:
        print("{} {}".format(start, end))
        return
    # 가장 큰 원반을 제외하고 나머지 원반들을 보조기둥으로 옮김
    hanoi(num -1, start, assist, end)
    print("{} {}".format(start, end))
    # 보조 기둥에서 목표기둥으로 다 옮김
    hanoi(num -1,assist,end,start)


num = int(input())
print(2**num-1)
if num <= 20:
    hanoi(num,1,3,2)
