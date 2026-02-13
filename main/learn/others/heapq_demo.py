import heapq

# 优先级队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Item-{self.name}'
    
# 堆排序
def sort_heap(arr:list):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

if __name__ == '__main__':
    # pq = PriorityQueue()
    # pq.push(Item('foo'), 1)
    # pq.push(Item('bar'), 5)
    # pq.push(Item('spam'), 4)
    # pq.push(Item('grok'), 1)
    # print(pq.pop())
    # print(pq.pop())
    # print(pq.pop())
    # print(pq.pop())
    print(sort_heap([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))