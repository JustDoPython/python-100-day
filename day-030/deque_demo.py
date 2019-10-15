from collections import deque
q = deque([1, 2, 3])
q.append('4')
q.appendleft('0')
print(q)

print(q.popleft())
