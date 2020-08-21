stack = [1,2,3,4]
print("Initial: " + str(stack))

#For LIFO, append to the end and pop when needed

stack.append(5)

print("Last in: " + str(stack))

stack.pop()

print("First out: " + str(stack))

#Creating a queue using listis inefficient since all elems need to be shifted due to FIFO
#Thus we use deque which is a double ended queue

from collections import deque

queue = deque([1,2,3,4])

print("Initial: " + str(queue))

queue.append(5)
print("First In: " + str(queue))

queue.popleft()
print("First Out: " + str(queue))