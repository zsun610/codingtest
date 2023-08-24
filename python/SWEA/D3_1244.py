T = int(input())

for tc in range(1,T+1):
    num,swap_num = map(int,input().split())
    num_arr = [i for i in num]
    tmp = sorted(num_arr,reverse=True)
    indexnum = []
    for i in range(len(num_arr)):
        for j in range(len(num_arr)):
            if num_arr[i] == tmp[j]:
                indexnum.append(j)