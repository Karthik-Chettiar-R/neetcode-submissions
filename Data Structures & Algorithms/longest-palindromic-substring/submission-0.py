class Solution:
    def longestPalindrome(self, s: str) -> str:

        currentLongestPalindrome=""
        

        for i in range(len(s)):
            
            # odd pali

            center=s[i]

            p1=i-1 
            p2=i+1

            currentLength=1

            while(p1>-1 and p2<len(s)):
                if s[p1]==s[p2]:
                    currentLength+=2
                    p1-=1
                    p2+=1

                else:
                    break

            if currentLength>len(currentLongestPalindrome):
                currentLength=len(currentLongestPalindrome)
                currentLongestPalindrome=s[p1+1:p2]



            # even pali

            p1=i
            p2=i+1

            currentLength=0

            while(p1>-1 and p2<len(s)):
                if s[p1]==s[p2]:
                    currentLength+=2
                    p1-=1
                    p2+=1

                else:
                    break

            if currentLength>len(currentLongestPalindrome):
                currentLength=len(currentLongestPalindrome)
                currentLongestPalindrome=s[p1+1:p2]


        return currentLongestPalindrome
    


        