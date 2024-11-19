"""
  deque is a collection type efficient for appending item from both      end. We can emulate 
    - stack for FIFO with append(item) & pop() ops
    - queue for LIFO with appendLeft(item) & popLeft() ops
"""
import collections

aDQue = collections.deque([10, 20, 30])

aDQue.appendleft(5)
aDQue.append(40)

print("Added to left and right", aDQue)

print("print 5?: ", aDQue.popleft())
print("print 40?: ", aDQue.pop())
