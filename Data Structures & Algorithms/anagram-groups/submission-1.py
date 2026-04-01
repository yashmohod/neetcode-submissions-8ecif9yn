class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s ={ }

        for i in strs:
            c = list(i)
            c.sort()
            c = "".join(c)
            if c in s:
                s[c].append(i)
            else:
                s[c] = [i]
        return list(s.values())