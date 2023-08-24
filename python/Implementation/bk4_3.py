start = input()

row = int(start[1])
col = start[0]
col_num = 99
col_type = ['a','b','c','d','e','f','g','h']

for i in range(len(col_type)):
    if col == col_type[i]:
        col_num = i+1
result = 0
# 상
if row >= 3:
    if 2 <= col_num <= 7:
        result += 2
    else:
        result += 1
# 하
if row <= 6:
    if 2 <= col_num <= 7:
        result += 2
    else:
        result += 1
# 좌
if col_num >= 3:
    if 2 <= row <= 7:
        result += 2
    else:
        result += 1
# 우
if col_num <= 3:
    if 2 <= row <= 7:
        result += 2
    else:
        result += 1

print(result)