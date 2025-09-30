from collections import deque
queue = deque([1])
queue.append(2)
# get 1
queue.popleft()

# get 2
queue.pop()