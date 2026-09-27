class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1

            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)

                if task != 0:
                    queue.append([task, time + n])
                
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time

            