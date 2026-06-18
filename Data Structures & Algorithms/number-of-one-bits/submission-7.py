class Solution:
    def hammingWeight(self, n: int) -> int:
        
        b=n
        r=0
        for i in range(32):
            b<<=i
            if n & 1<<i >0:
                r+=1
        return r

            