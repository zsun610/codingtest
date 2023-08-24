# 기둥은 항상 좌표에서 위로 설치, 보는 항상 좌표에서 오른쪽으로 설치
def solution(n, build_frame):
    gidoongs = []
    bos = []
    for i in range(len(build_frame)):
        x = build_frame[i][0]
        y = build_frame[i][1]
        construction = build_frame[i][3]
        # 설치
        if construction == 1:
            if build_frame[i][2] == 0:  # 기둥 설치
                # 1.바닥 위에
                if y == 0:
                    gidoongs.append([x, y, 0])
                # 2.보의 한쪽 끝 부분 위에 : (x-1,y)이 bos에 있어야 -> 보는 항상 오른쪽으로 설치
                elif [x - 1, y, 1] in bos:
                    gidoongs.append([x, y, 0])
                # 3.기둥 위에 : (x,y-1) 이 gidoongs에 있어야
                elif [x, y - 1, 0] in gidoongs:
                    gidoongs.append([x, y, 0])

            else:  # 보 설치
                # 1.보 설치하려는 한쪽 끝부분 (왼쪽(x,y+1) or 오른쪽(x+1,y)) gidoongs에 있어야
                if [x, y - 1, 0] in gidoongs or [x + 1, y - 1, 0] in gidoongs:
                    bos.append([x, y, 1])
                # 2. (x-1,y) and (x+1,y)가 bos에 있어야
                elif [x - 1, y, 1] in bos and [x + 1, y, 1] in bos:
                    bos.append([x, y, 1])

        # 삭제
        else:  # 삭제해도 될 때
            if build_frame[i][2] == 0:  # 기둥
                # 1. 기둥 양쪽에 보가 있을 때
                if [x, y + 1, 1] in bos and [x - 1, y + 1, 1] in bos:
                    gidoongs.remove([x, y, 0])
                    # 2. 양쪽에 보가 없을 때 - 위에 기둥이 없을 때 (기둥이 우뚝 서 있을 때)
                else:
                    if [x, y + 1, 0] not in gidoongs:
                        gidoongs.remove([x, y, 0])
            else:  # 보
                # 1. 보에 연결된 보이면서 양쪽에 기둥 (3개 중 가운데 보만 없어도 됨- 사이에 낑긴 보) 4개 이상일 때눈? 안됨
                if [x - 1, y, 1] in bos and [x + 1, y, 1] in bos and [x - 1, y - 1, 0] in gidoongs and [x + 2, y - 1, 0] in gidoongs:
                    bos.remove([x, y, 1])

    answer = sorted(gidoongs + bos)

    return answer

# build_frame = [x,y,a,b]
# x,y = 좌표, a: 0-기둥, 1-보, b: 0-삭제, 1-설치