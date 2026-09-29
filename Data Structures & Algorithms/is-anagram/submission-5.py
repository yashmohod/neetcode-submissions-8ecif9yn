class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = 0
        for i in s:
            r = r ^ ord(i)
        for i in t:             
            r = r ^ ord(i)

        print(r)
        return r == 0
