class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newS=""

        for i in range(len(s)):
            if s[i].isalnum() and s[i].isalpha():
                newS+=s[i].lower()

            elif s[i].isalnum():
                newS+=s[i]

        s=newS
        i=0
        j=len(s)-1

      



        while(i<j):
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False

        return True