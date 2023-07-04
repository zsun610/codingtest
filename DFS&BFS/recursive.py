# 반복적으로 구현한 n! ( return 1번 - 최종 반환값)
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

# 재귀적으로 구현한 n! ( return 2번 이상 - 최종 반환값, 재귀 반환값)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(5),factorial_recursive(5))