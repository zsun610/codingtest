def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:    # 설치된 것이 '기둥'
            # 기둥 설치 가능 : 1.바닥 위 2. 보의 왼쪽 or 오른쪽 위 3. 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        elif stuff == 1:  # 설치된 것이 '보'
            # 보 설치 가능 : 1. 왼쪽 or 오른쪽 끝부분이 기둥 위  2.'양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n,build_frame):
    answer = []
    # 돌때마다 건물전체 확인
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:  # 삭제
            answer.remove([x,y,stuff])  # 일단 삭제 갈겨
            if not possible(answer):    # 삭제 불가?
                answer.append([x,y,stuff])   # 그럼 다시 추가
        if operate == 1:  # 설치
            answer.append([x,y,stuff])   # 일단 설치 갈겨
            if not possible(answer):     # 설치 불가?
                answer.remove([x,y,stuff])  # 그럼 다시 삭제
    return sorted(answer)