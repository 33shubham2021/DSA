"""
This has implementatin of priority queue via library in Python
heapq - min priority queue
        If you need a max-priority queue (where the largest number comes out 
        first), the common trick is to negate the numbers when pushing them 
        into the heap.

If you want to store objects with a priority, use a tuple: (priority, data). 
Python will compare the first element of the tuple first.
PriorityQueue
    1. qsize()
    2. empty()
    3. put()
    4. get()
"""
import heapq
from queue import PriorityQueue

if __name__ == "__main__":
    pq = []
    heapq.heappush(pq, 10)
    heapq.heappush(pq, 5)
    heapq.heappush(pq, 20)

    # Peek at the smallest element
    print(pq[0])  # Output: 5

    smallest = heapq.heappop(pq)
    print(smallest)  # Output: 5

    tasks = []
    heapq.heappush(tasks, (2, "Write code"))
    heapq.heappush(tasks, (1, "Fix critical bug"))
    heapq.heappush(tasks, (3, "Attend meeting"))

    # Pop by priority
    priority, task = heapq.heappop(tasks)
    print(f"Doing: {task}") # Output: Doing: Fix critical bug

    q = PriorityQueue()
    q.put((2, "Priority 2"))
    q.put((5, "Priority 5"))
    q.put((3, "Priority 3"))

    print(q.get())

    q1 = PriorityQueue()
    q1.put(1)
    q1.put(7)
    q1.put(3)
    q1.put(5)
    while not q1.empty():
        print(q1.get())

