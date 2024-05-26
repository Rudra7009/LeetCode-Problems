class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2 :
            return False
        l = len(s)
        if l <= 2 :
            return True
        for i in range(l - 2) :
            if s[i] == s[i+1] == s[i+2] == "L" :
                return False
        return True
