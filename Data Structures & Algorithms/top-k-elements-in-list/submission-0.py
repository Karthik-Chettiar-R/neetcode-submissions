import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]

        frequency={}

        for i in range(len(nums)):
            if nums[i] not in frequency:
                frequency[nums[i]]=1
            else:
                frequency[nums[i]]+=1
        
        for key in frequency :
            heapq.heappush(heap,(-frequency[key],key))
        ret=[]
        for i in range(k):
            ret.append(heapq.heappop(heap)[1])

        return ret

