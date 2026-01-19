"""
Docstring for heaps.heap
max_heapify - time complexity = O(log n)
1st leaf = floor(n/2) + 1, for 1-indexed arrays
           floor(n/2)      for 0-indexed arrays
why bottom up build - Subtrees are already heaps before parent is heapified
time complexity of build_max_heap - O(n)
arr.pop(), del arr[n-1] - removes last element 
sorting problem - https://leetcode.com/problems/sort-an-array/

insert and delete from a heap -. TODO
create a complete heap class, supporting all the operations TODO

h = Heap([] , MAX_HEAP/MIN_HEAP)
heap.insert(element)
heap.delete(element)
heap.get_max()
heap.heap_sort() -> returns a sorted array

create a generic priority queue class using heaps TODO


"""
#in descending order
def heap_sort(arr):
    ans = []
    build_max_heap(arr)
    while(len(arr) > 0):
        n = len(arr)
        arr[0],arr[n-1] = arr[n-1],arr[0]
        ans.append(arr.pop())
        max_heapify(arr , 0)
    return ans


def build_max_heap(arr):
    n = len(arr)
    # 1st leaf is at index=n/2
    i = (n // 2) - 1
    while (i >= 0):
        max_heapify(arr , i)
        i -= 1

def build_min_heap(arr):
    n = len(arr)
    # 1st leaf is at index=n/2
    i = (n // 2) - 1
    while (i >= 0):
        min_heapify(arr , i)
        i -= 1

# Iterative Version
def max_heapify(heap , index):
    l = len(heap)
    while True:
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < l and heap[left] > heap[largest]:
            largest = left
        if right < l and heap[right] > heap[largest]:
            largest = right
            
        if largest == index:
            break
            
        swap(heap , index, largest)
        index = largest

# Min Heapify        
def min_heapify(heap , index):
    l = len(heap)
    while True:
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < l and heap[left] < heap[smallest]:
            smallest = left
        if right < l and heap[right] < heap[smallest]:
            smallest = right
            
        if smallest == index:
            break
            
        swap(heap , index, smallest)
        index = smallest
    
def max_heapify_recursive(heap , index):
    l = len(heap)
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < l and heap[left] > heap[largest]:
        largest = left

    if right < l and heap[right] > heap[largest]:
        largest = right

    if largest != index:
        swap(heap, index, largest)
        max_heapify(heap, largest)

def swap(arr , first, second):
    arr[first],arr[second] = arr[second], arr[first]

def main():
    arr1 = [90, 70, 80, 60, 100, 75, 65]
    # o/p - [90, 100, 80, 60, 70, 75, 65]

    arr2 = [50, 90, 80, 70, 60, 75, 65]
    # o/p - [90, 70, 80, 50, 60, 75, 65]

    #max_heapify_recursive(arr , 1)
    # max_heapify(arr1 , 1)
    # max_heapify(arr2 , 0)
    # arr = [3, 1, 6, 5, 2, 4] # expected = [6, 5, 4, 1, 2, 3]
    # build_max_heap(arr)
    arr = [3, 1, 6, 5, 2, 4]
    sortedArray = heap_sort(arr)
    print(sortedArray)
    


if __name__ == '__main__':
    main()


"""
Time and space complexities 
| Operation                   | Description                 | Time Complexity        | Extra Space        |
| --------------------------- | --------------------------- | ---------------------- | ------------------ |
| **Build Max / Min Heap**    | Convert array into heap     | **O(n)**               | O(1)               |
| **Heapify (max/min)**       | Fix heap at index `i`       | **O(log n)**           | O(1) *(iterative)* |
|                             |                             | O(log n) *(recursive)* |                    |
| **Insert (Push)**           | Insert new element          | **O(log n)**           | O(1)               |
| **Extract Max / Min**       | Remove root                 | **O(log n)**           | O(1)               |
| **Increase / Decrease Key** | Modify key value            | **O(log n)**           | O(1)               |
| **Peek (Get Max / Min)**    | Access root                 | **O(1)**               | O(1)               |
| **Delete arbitrary index**  | Delete element at index `i` | **O(log n)**           | O(1)               |
| **Heap Sort**               | Sorting using heap          | **O(n log n)**         | O(1)               |

"""