from collections import deque

# 큐(queue)(선입선출)구현을 위해 deque 라이브러리 사용
queue = deque()

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)     #먼저 들어온 순서대로 출력, deque([3, 7, 1, 4])
queue.reverse()  #다음 출력을 위해 역순
print(queue)     #나중에 들어온 원소부터 출력, deque([4, 1, 7, 3])

#stack (후입선출) - 리스트
stack = []

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)         # [5, 2, 3, 1]
print(stack[::-1])   # [1, 3, 2, 5]
