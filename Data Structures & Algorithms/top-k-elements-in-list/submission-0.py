class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        maxHeap = []
        for key in counts:
            maxHeap.append((counts[key]*-1, key))
        heapq.heapify(maxHeap)
        res = []
        for n in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res