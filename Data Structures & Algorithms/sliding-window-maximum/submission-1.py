import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        maxHeap = []
        for i in range(len(nums)):
            heapq.heappush(maxHeap,-nums[i])
            if i >= k-1 :
                ans.append(-maxHeap[0])
                maxHeap.remove(-nums[i-k+1])
                heapq.heapify(maxHeap)

        return ans