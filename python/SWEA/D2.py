T = int(input())

for test_case in range(1,T+1):
    n = str(input())
    result = 'No'
    for i in range(2):
        if n[i] == '9':
            result = 'Yes'
    print("#"+str(test_case)+" "+result)

