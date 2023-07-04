# 피보나치 수열 - 반복, Bottom-up

# DP테이블 초기화
d = [0]*100
# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 반복문으로 구현 (Bottom-up 다이나믹 프로그래밍)
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])