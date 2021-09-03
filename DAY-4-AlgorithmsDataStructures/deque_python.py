from collections import deque

# Deque - can insert both at the beginning and the end
# similar to list but insert is faster

dq = deque()
dq.append('a')
dq.appendleft('z')
dq.extend([2, 17])
print(dq)
dq.extendleft({'t', 17})
print(dq)
dq.pop()
dq.popleft()
print(dq)
print(dq[2])
# print(dq[2:])  # fail, deque can not slice
