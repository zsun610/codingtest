# x

num = int(input())

arr = []
for i in range(num):
    input_data = input().split()
    # 리스트에 (이름,점수) 한 쌍을 튜플로 저장
    arr.append((input_data[0],int(input_data[1])))

arr.sort(key=lambda student:student[1])

for student in arr:
    print(student[0], end= ' ')