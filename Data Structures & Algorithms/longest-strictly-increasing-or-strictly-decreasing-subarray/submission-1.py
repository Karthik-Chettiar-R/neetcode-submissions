class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m1=1
        m2=1
        i=0
        j=0
        s=1
        curr=i
        while(j<len(nums) and i<len(nums)):
            
            if j+1<len(nums) and nums[j+1]>nums[curr]:
                j=j+1
                s+=1
                curr=j
                m1=max(m1,s)
            else :
                if i+1>j:
                    j+=1
                    i+=1
                    curr=j
                    s=1
                else :
                    i+=1
                    s=abs(i-j)+1
        i=0
        j=0
        s=1
        curr=i
        while(j<len(nums) and i<len(nums)):
            
            if j+1<len(nums) and curr<len(nums) and nums[j+1]<nums[curr]:
                j=j+1
                s+=1
                m2=max(m2,s)
                curr=j
            else :
                if i+1>j:
                    j+=1
                    i+=1
                    s=1
                    curr=j
                else :
                    i+=1
                    s=abs(i-j)+1
        return max(m1,m2)
        

                