class MedianFinder:

    def __init__(self):
        self.bottomHalf = [] #max heap
        self.topHalf = [] # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.bottomHalf, -num)

        n = -heapq.heappop(self.bottomHalf)
        heapq.heappush(self.topHalf, n)

        if len(self.topHalf) > len(self.bottomHalf):
            n = heapq.heappop(self.topHalf)
            heapq.heappush(self.bottomHalf, -n)


    def findMedian(self) -> float:
        if len(self.bottomHalf) > len(self.topHalf):
            return -self.bottomHalf[0]
        else:
            return (-self.bottomHalf[0] + self.topHalf[0]) / 2
        