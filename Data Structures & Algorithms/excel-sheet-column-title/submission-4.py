class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        while(columnNumber>26):
            s+=chr(64+columnNumber%26)
            columnNumber//=26
        if columnNumber>0:
            s+=chr(columnNumber+64)
        return s[::-1]

        